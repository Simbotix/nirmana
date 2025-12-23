# Nirmana - Business Logic & Functions

All calculation logic, workflows, and API specifications.

---

## Platform Fee Calculation

```python
def calculate_platform_fee(booking_items):
    """
    10% platform fee on ALL lister transactions.
    Only exception: Site owner (is_owner=True) keeps 100%.

    Args:
        booking_items: List of Nirmana Booking Item records

    Returns:
        Decimal: Total platform fee
    """
    total_fee = 0

    for item in booking_items:
        if not item.lister.is_owner:
            total_fee += item.line_total * 0.10

    return total_fee
```

---

## Delivery Cost Calculation

```python
def calculate_delivery_cost(origin_zip, destination_zip):
    """
    Calculate delivery fee based on ZIP code distance.

    Args:
        origin_zip: Item location ZIP code
        destination_zip: Customer delivery ZIP code

    Returns:
        Decimal or None: Delivery fee, or None if out of range

    Pricing:
        - Base fee: $10.00
        - Per mile: $0.50
        - Max radius: 50 miles
    """
    distance_miles = get_distance_between_zips(origin_zip, destination_zip)

    if distance_miles > 50:
        return None  # Out of delivery range

    base_fee = 10.00
    per_mile = 0.50

    return base_fee + (distance_miles * per_mile)


def get_distance_between_zips(zip1, zip2):
    """
    Calculate distance between two ZIP codes.
    Uses ZIP code centroid coordinates.

    Options:
        1. Use ZIP code database with lat/lng
        2. Use Google Maps Distance Matrix API
        3. Use free ZIP code API
    """
    # Get coordinates for both ZIPs
    coord1 = get_zip_coordinates(zip1)
    coord2 = get_zip_coordinates(zip2)

    # Haversine formula for distance
    return haversine_distance(coord1, coord2)
```

---

## Deposit Calculation

```python
def calculate_deposit(booking_items):
    """
    Deposit based on total order value.
    Tiered percentage system.

    Args:
        booking_items: List of Nirmana Booking Item records

    Returns:
        Decimal: Required deposit amount

    Tiers:
        - Under $100: 50% deposit
        - $100-$500: 30% deposit
        - Over $500: 20% deposit
    """
    total_value = sum(item.line_total for item in booking_items)

    if total_value < 100:
        return total_value * 0.50  # 50% for small orders
    elif total_value < 500:
        return total_value * 0.30  # 30% for medium orders
    else:
        return total_value * 0.20  # 20% for large orders
```

---

## Booking Total Calculation

```python
def calculate_booking_total(booking):
    """
    Calculate all totals for a booking.

    Returns dict with:
        - subtotal: Sum of all item line totals
        - platform_fee: 10% of non-owner items
        - delivery_fee: If delivery selected
        - deposit_amount: Based on subtotal
        - grand_total: subtotal + delivery_fee (deposit separate)
    """
    subtotal = sum(item.line_total for item in booking.items)
    platform_fee = calculate_platform_fee(booking.items)

    delivery_fee = 0
    if booking.delivery_type == "Delivery":
        # Get the furthest item's ZIP for calculation
        for item in booking.items:
            fee = calculate_delivery_cost(
                item.item.location_zip,
                booking.delivery_zip
            )
            if fee and fee > delivery_fee:
                delivery_fee = fee

    deposit_amount = calculate_deposit(booking.items)

    grand_total = subtotal + delivery_fee

    return {
        "subtotal": subtotal,
        "platform_fee": platform_fee,
        "delivery_fee": delivery_fee,
        "deposit_amount": deposit_amount,
        "grand_total": grand_total
    }
```

---

## Rental Duration Calculation

```python
def calculate_rental_days(start_date, end_date):
    """
    Calculate number of rental days (inclusive).
    Minimum 1 day.

    Args:
        start_date: Rental start date
        end_date: Rental end date

    Returns:
        int: Number of days
    """
    delta = end_date - start_date
    days = delta.days + 1  # Inclusive
    return max(1, days)


def calculate_item_price(item, days):
    """
    Calculate best price for rental duration.
    Auto-selects weekly rate if beneficial.

    Args:
        item: Nirmana Item record
        days: Number of rental days

    Returns:
        Decimal: Total rental price
    """
    daily_total = item.daily_rate * days

    # Check if weekly rate is better
    if days >= 7 and item.weekly_rate:
        weeks = days // 7
        remaining_days = days % 7
        weekly_total = (weeks * item.weekly_rate) + (remaining_days * item.daily_rate)

        if weekly_total < daily_total:
            return weekly_total

    return daily_total
```

---

## Availability Check

```python
def check_item_availability(item_id, start_date, end_date, quantity=1):
    """
    Check if item is available for given dates.

    Args:
        item_id: Nirmana Item ID
        start_date: Requested start date
        end_date: Requested end date
        quantity: How many needed

    Returns:
        dict: {
            "available": bool,
            "available_quantity": int,
            "conflicting_bookings": list
        }
    """
    item = frappe.get_doc("Nirmana Item", item_id)

    if item.status == "Unavailable":
        return {"available": False, "available_quantity": 0, "conflicting_bookings": []}

    # Find overlapping confirmed bookings
    overlapping = frappe.get_all(
        "Nirmana Booking Item",
        filters={
            "item": item_id,
            "parent": ["in",
                frappe.get_all("Nirmana Booking",
                    filters={
                        "status": ["in", ["Confirmed", "Picked Up"]],
                        "start_date": ["<=", end_date],
                        "end_date": [">=", start_date]
                    },
                    pluck="name"
                )
            ]
        },
        fields=["quantity", "parent"]
    )

    booked_quantity = sum(b.quantity for b in overlapping)
    available_quantity = item.quantity - booked_quantity

    return {
        "available": available_quantity >= quantity,
        "available_quantity": available_quantity,
        "conflicting_bookings": [b.parent for b in overlapping]
    }
```

---

## Lister Payout Calculation

```python
def calculate_lister_payout(lister_id, start_date, end_date):
    """
    Calculate payout for a lister for given period.

    Args:
        lister_id: Nirmana Lister ID
        start_date: Period start
        end_date: Period end

    Returns:
        dict: {
            "gross_amount": Decimal,
            "platform_fee": Decimal,
            "net_amount": Decimal,
            "bookings": list
        }
    """
    lister = frappe.get_doc("Nirmana Lister", lister_id)

    # Get all completed bookings in period
    booking_items = frappe.get_all(
        "Nirmana Booking Item",
        filters={
            "lister": lister_id,
            "parent": ["in",
                frappe.get_all("Nirmana Booking",
                    filters={
                        "status": "Returned",
                        "end_date": ["between", [start_date, end_date]]
                    },
                    pluck="name"
                )
            ]
        },
        fields=["line_total", "parent"]
    )

    gross_amount = sum(item.line_total for item in booking_items)

    # Owner pays no fee
    if lister.is_owner:
        platform_fee = 0
    else:
        platform_fee = gross_amount * 0.10

    net_amount = gross_amount - platform_fee

    return {
        "gross_amount": gross_amount,
        "platform_fee": platform_fee,
        "net_amount": net_amount,
        "bookings": list(set(item.parent for item in booking_items))
    }
```

---

## API Endpoints

### Public APIs (allow_guest=True)

```python
@frappe.whitelist(allow_guest=True)
def search_items(category=None, zip_code=None, radius=50, query=None):
    """
    Search items by category, location, or text.

    Args:
        category: Nirmana Category name
        zip_code: Customer ZIP for distance filtering
        radius: Max miles from ZIP (default 50)
        query: Text search in name/description

    Returns:
        list: Matching items with distance
    """
    pass


@frappe.whitelist(allow_guest=True)
def get_item_details(item_id):
    """
    Get full item details including lister info.
    """
    pass


@frappe.whitelist(allow_guest=True)
def check_availability(item_id, start_date, end_date, quantity=1):
    """
    Check if item is available for dates.
    """
    pass


@frappe.whitelist(allow_guest=True)
def calculate_delivery(origin_zip, destination_zip):
    """
    Get delivery cost estimate.
    """
    pass


@frappe.whitelist(allow_guest=True)
def get_categories():
    """
    Get all categories with item counts.
    """
    pass
```

### Authenticated APIs

```python
@frappe.whitelist()
def create_booking(items, start_date, end_date, delivery_type, delivery_address=None):
    """
    Create a new booking.

    Args:
        items: List of {item_id, quantity}
        start_date: Rental start
        end_date: Rental end
        delivery_type: "Pickup" or "Delivery"
        delivery_address: Required if delivery

    Returns:
        dict: Booking details with payment info
    """
    pass


@frappe.whitelist()
def create_payment_intent(booking_id):
    """
    Create Stripe PaymentIntent for booking.
    """
    pass


@frappe.whitelist()
def confirm_booking(booking_id, payment_intent_id):
    """
    Confirm booking after successful payment.
    """
    pass


@frappe.whitelist()
def cancel_booking(booking_id, reason=None):
    """
    Cancel a booking. Refund if applicable.
    """
    pass


@frappe.whitelist()
def add_to_wishlist(item_id, notify_available=False):
    """
    Add item to user's wishlist.
    """
    pass


@frappe.whitelist()
def remove_from_wishlist(item_id):
    """
    Remove item from wishlist.
    """
    pass


@frappe.whitelist()
def get_wishlist():
    """
    Get user's wishlist items.
    """
    pass


@frappe.whitelist()
def send_message(conversation_id=None, lister_id=None, item_id=None, message=None):
    """
    Send message in conversation.
    Creates new conversation if needed.
    """
    pass


@frappe.whitelist()
def get_conversations():
    """
    Get user's conversations (as renter or lister).
    """
    pass


@frappe.whitelist()
def mark_conversation_read(conversation_id):
    """
    Mark conversation as read.
    """
    pass
```

### Lister APIs

```python
@frappe.whitelist()
def get_lister_dashboard():
    """
    Get lister's dashboard data.

    Returns:
        - Active listings
        - Pending bookings
        - Recent earnings
        - Unread messages
    """
    pass


@frappe.whitelist()
def create_listing(item_data):
    """
    Create new item listing.
    """
    pass


@frappe.whitelist()
def update_listing(item_id, item_data):
    """
    Update existing listing.
    """
    pass


@frappe.whitelist()
def toggle_listing_status(item_id, status):
    """
    Change listing availability.
    """
    pass


@frappe.whitelist()
def get_lister_earnings(period="month"):
    """
    Get earnings summary.
    """
    pass


@frappe.whitelist()
def connect_stripe_account():
    """
    Start Stripe Connect onboarding.
    Returns Stripe Connect URL.
    """
    pass
```

### Webhook Handlers

```python
@frappe.whitelist(allow_guest=True)
def stripe_webhook():
    """
    Handle Stripe webhook events.

    Events:
        - payment_intent.succeeded: Confirm booking
        - payment_intent.payment_failed: Handle failure
        - transfer.created: Track lister payout
        - charge.refunded: Track deposit refund
        - account.updated: Lister Stripe status
    """
    pass
```

---

## Notifications

### Email Triggers

| Event | Recipient | Template |
|-------|-----------|----------|
| Booking Confirmed | Customer | booking_confirmed |
| Booking Confirmed | Lister | new_booking_lister |
| Pickup Reminder | Customer | pickup_reminder |
| Return Reminder | Customer | return_reminder |
| Booking Returned | Lister | booking_returned |
| Deposit Refunded | Customer | deposit_refunded |
| Payout Sent | Lister | payout_sent |
| New Message | Recipient | new_message |
| Item Available | Wishlist User | item_available |

### Notification Logic

```python
def send_pickup_reminder():
    """
    Daily job: Send reminder for pickups tomorrow.
    """
    tomorrow = add_days(today(), 1)

    bookings = frappe.get_all("Nirmana Booking",
        filters={
            "status": "Confirmed",
            "delivery_type": "Pickup",
            "start_date": tomorrow
        }
    )

    for booking in bookings:
        send_email_template("pickup_reminder", booking)


def send_return_reminder():
    """
    Daily job: Send reminder for returns tomorrow.
    """
    tomorrow = add_days(today(), 1)

    bookings = frappe.get_all("Nirmana Booking",
        filters={
            "status": "Picked Up",
            "end_date": tomorrow
        }
    )

    for booking in bookings:
        send_email_template("return_reminder", booking)


def notify_wishlist_available(item_id):
    """
    Notify users when wishlisted item becomes available.
    """
    wishlist_items = frappe.get_all("Nirmana Wishlist Item",
        filters={
            "item": item_id,
            "notify_available": 1
        },
        fields=["user"]
    )

    for wi in wishlist_items:
        send_email_template("item_available", {
            "user": wi.user,
            "item": item_id
        })
```

---

## Scheduled Jobs

| Frequency | Function | Description |
|-----------|----------|-------------|
| Daily 8am | send_pickup_reminder | Remind pickups tomorrow |
| Daily 8am | send_return_reminder | Remind returns tomorrow |
| Daily 9am | check_overdue_bookings | Flag overdue returns |
| Weekly | process_lister_payouts | Send weekly payouts |
| Monthly | generate_platform_report | Platform analytics |
