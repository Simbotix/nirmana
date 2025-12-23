# Nirmaha - Business Requirements

## Overview

Equipment rental management system for sister's rental business. March 2025 deadline for community showcase.

## Core Workflows

### 1. Equipment Lifecycle

```
Purchase → Available → Rented → Returned → Available
                ↓           ↓
           Maintenance   Damaged → Repair → Available
                              ↓
                           Retired
```

### 2. Rental Flow

```
Customer Inquiry
     ↓
Check Availability
     ↓
Create Booking (Reserved)
     ↓
Collect Deposit
     ↓
Checkout (Equipment handed over)
     ↓
Return (Equipment received back)
     ↓
Inspection
     ↓
├── No Damage → Full deposit refund
└── Damage → Damage Report → Deduct from deposit → Partial refund
     ↓
Generate Invoice
     ↓
Payment (if balance due)
```

## DocType Specifications

### Rental Equipment

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| equipment_name | Data | Yes | Display name |
| equipment_code | Data | Yes | Unique code (auto-generated) |
| category | Link: Rental Category | Yes | Equipment category |
| status | Select | Yes | Available/Rented/Maintenance/Retired |
| location | Link: Rental Location | No | Current warehouse location |
| purchase_date | Date | No | When purchased |
| purchase_price | Currency | No | Original cost |
| hourly_rate | Currency | No | Rental rate per hour |
| daily_rate | Currency | Yes | Rental rate per day |
| weekly_rate | Currency | No | Rental rate per week |
| monthly_rate | Currency | No | Rental rate per month |
| deposit_amount | Currency | Yes | Security deposit required |
| description | Text Editor | No | Detailed description |
| images | Attach | No | Equipment photos |
| qr_code | Attach | No | Auto-generated QR code |
| condition_notes | Text | No | Current condition |

### Rental Customer

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| customer_name | Data | Yes | Full name |
| phone | Data | Yes | Primary phone (for SMS) |
| email | Data | No | Email address |
| id_type | Select | Yes | Aadhaar/PAN/Driving License |
| id_number | Data | Yes | ID document number |
| id_proof | Attach | Yes | Scanned ID document |
| address | Text | Yes | Full address |
| city | Data | Yes | City |
| pincode | Data | Yes | PIN code |
| total_rentals | Int | No | Count of rentals (auto) |
| total_revenue | Currency | No | Total spent (auto) |
| blacklisted | Check | No | Block this customer |
| blacklist_reason | Text | No | Why blacklisted |

### Rental Booking

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| booking_id | Data | Yes | Auto-generated ID |
| customer | Link: Rental Customer | Yes | Customer |
| status | Select | Yes | Reserved/Confirmed/Checked Out/Returned/Cancelled |
| booking_date | Date | Yes | When booking was made |
| start_date | Date | Yes | Rental start date |
| end_date | Date | Yes | Rental end date |
| equipment_items | Table: Booking Item | Yes | List of equipment |
| rate_type | Select | Yes | Hourly/Daily/Weekly/Monthly |
| subtotal | Currency | No | Calculated total |
| discount_percent | Percent | No | Discount applied |
| discount_amount | Currency | No | Discount in currency |
| tax_amount | Currency | No | GST if applicable |
| grand_total | Currency | No | Final amount |
| deposit_required | Currency | No | Total deposit needed |
| notes | Text | No | Special instructions |

### Rental Checkout

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| checkout_id | Data | Yes | Auto-generated |
| booking | Link: Rental Booking | Yes | Related booking |
| checkout_datetime | Datetime | Yes | When equipment handed over |
| checked_out_by | Link: User | Yes | Staff who processed |
| condition_at_checkout | Text | No | Equipment condition notes |
| photos_at_checkout | Attach | No | Photos of equipment |
| customer_signature | Signature | No | Customer acknowledgment |
| deposit_collected | Currency | No | Deposit amount received |
| deposit_payment_mode | Select | No | Cash/UPI/Card/Bank Transfer |

### Rental Return

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| return_id | Data | Yes | Auto-generated |
| booking | Link: Rental Booking | Yes | Related booking |
| checkout | Link: Rental Checkout | Yes | Related checkout |
| return_datetime | Datetime | Yes | When returned |
| received_by | Link: User | Yes | Staff who received |
| condition_at_return | Text | No | Condition notes |
| photos_at_return | Attach | No | Photos of equipment |
| has_damage | Check | No | Damage found? |
| damage_report | Link: Rental Damage Report | No | If damaged |
| late_hours | Float | No | Hours past due |
| late_fee | Currency | No | Late return fee |

### Rental Damage Report

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| damage_id | Data | Yes | Auto-generated |
| booking | Link: Rental Booking | Yes | Related booking |
| equipment | Link: Rental Equipment | Yes | Damaged equipment |
| reported_datetime | Datetime | Yes | When reported |
| damage_description | Text | Yes | What's damaged |
| damage_photos | Attach | Yes | Photo evidence |
| repair_cost_estimate | Currency | No | Estimated repair cost |
| deduct_from_deposit | Currency | No | Amount to deduct |
| customer_acknowledged | Check | No | Customer agreed? |

### Rental Invoice

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| invoice_id | Data | Yes | Auto-generated |
| booking | Link: Rental Booking | Yes | Related booking |
| customer | Link: Rental Customer | Yes | Customer |
| invoice_date | Date | Yes | Invoice date |
| due_date | Date | No | Payment due date |
| rental_amount | Currency | Yes | Base rental |
| late_fee | Currency | No | Late return charges |
| damage_charges | Currency | No | Damage deductions |
| deposit_collected | Currency | No | Deposit paid |
| deposit_refunded | Currency | No | Deposit returned |
| deposit_adjusted | Currency | No | Deposit used for charges |
| subtotal | Currency | No | Before tax |
| tax_amount | Currency | No | GST |
| grand_total | Currency | Yes | Total payable |
| amount_paid | Currency | No | Amount received |
| balance | Currency | No | Outstanding |
| status | Select | Yes | Draft/Unpaid/Paid/Cancelled |

## Pricing Logic

### Rate Selection
```python
def calculate_rental_price(equipment, duration_days, rate_type="auto"):
    if rate_type == "auto":
        # Auto-select best rate for customer
        if duration_days >= 30 and equipment.monthly_rate:
            months = ceil(duration_days / 30)
            return months * equipment.monthly_rate
        elif duration_days >= 7 and equipment.weekly_rate:
            weeks = ceil(duration_days / 7)
            return weeks * equipment.weekly_rate
        else:
            return duration_days * equipment.daily_rate
    # ... explicit rate selection
```

### Late Fees
- Grace period: 2 hours
- After grace: 10% of daily rate per hour
- Max late fee: 2x daily rate

### Deposit Rules
- Minimum: 1 day rental amount
- Maximum: 50% of equipment value
- Refund within 24 hours of return (if no damage)

## Notifications

### SMS Templates

| Event | Template |
|-------|----------|
| Booking Confirmed | "Your booking #{booking_id} is confirmed. Pickup: {date} at {location}. Deposit: Rs{amount}" |
| Pickup Reminder | "Reminder: Pickup tomorrow for booking #{booking_id}. Time: {time}. Bring ID proof." |
| Return Reminder | "Reminder: Return due tomorrow for booking #{booking_id}. Avoid late fees!" |
| Overdue Alert | "URGENT: Your rental #{booking_id} is overdue. Late fees applying. Return ASAP." |
| Payment Received | "Payment of Rs{amount} received for invoice #{invoice_id}. Thank you!" |

## Reports Required

1. **Daily Operations**: Today's pickups, returns, overdue
2. **Equipment Utilization**: Usage % per equipment
3. **Revenue Report**: Daily/Weekly/Monthly revenue
4. **Customer Report**: Top customers, blacklisted
5. **Inventory Report**: Equipment by status, maintenance due

## Permissions Matrix

| Role | Equipment | Booking | Checkout/Return | Invoice | Settings |
|------|-----------|---------|-----------------|---------|----------|
| Administrator | CRUD | CRUD | CRUD | CRUD | CRUD |
| Manager | CRUD | CRUD | CRUD | CRUD | Read |
| Staff | Read | Create/Read | CRUD | Read | None |
| Customer (Portal) | Read | Create/Read own | None | Read own | None |

## Integration Points

### Razorpay
- Collect deposits online
- Invoice payments
- Webhook for payment confirmation

### SMS (MSG91)
- Transactional SMS for all notifications
- DLT registration required for India

### QR Codes
- Generate QR for each equipment
- QR links to equipment detail page
- Staff can scan to pull up equipment info
