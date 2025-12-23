# Nirmaha - Business Requirements

## Overview

**Nirmaha** is a peer-to-peer rental marketplace for props, party supplies, and event inventory. Built on Frappe Framework with a South Indian festive theme (rangoli, lotuses, banana leaves, subtle colors).

| Attribute | Value |
|-----------|-------|
| **Platform Type** | Peer-to-peer rental marketplace |
| **Owner** | Shilpa |
| **IT Admin** | Rajesh |
| **Theme** | South Indian festive (rangoli, lotuses, banana leaves) |
| **Target Market** | US-based (50-mile delivery radius) |
| **Payment Gateway** | Stripe |

## User Roles

| Role | Description | Permissions |
|------|-------------|-------------|
| **Site Owner** | Shilpa - controls most listings, day-to-day operations | Full access to all features |
| **IT Admin** | Rajesh - technical support, not daily operations | System configuration, no operational tasks |
| **Listers** | Friends/peers who add their own listings | Create/manage own listings, view own earnings |
| **Renters/Customers** | General users who rent items | Browse, book, pay, leave reviews |

## Core Features

### 1. Item Listings
- Props (decorations, backdrops, staging items)
- Add-ons (lights, figurines, accessories)
- Party supplies
- DIY/how-to videos attached to items
- Multiple images per listing
- Condition documentation

### 2. Multi-Vendor Marketplace
- **Invite-only listers** - only Shilpa (site owner) can create lister accounts
- No self-signup for listers (controlled onboarding)
- Each lister has their own profile/storefront
- Platform takes **10% fee on ALL lister transactions** (except Shilpa's own listings)
- Listers set their own prices
- All listers coordinate with Shilpa

### 3. Geotagging & Delivery
- Location info on all listings
- Delivery within 50-mile radius
- Delivery cost calculator based on distance
- Pickup option available

### 4. Payments & Fees
- Stripe integration for payments
- 10% platform fee on partner listings
- Refundable deposit based on total order value
- Multi-item orders from different locations supported

### 5. In-App Messaging
- Renters can message listers about items
- Listers can respond to inquiries
- Message thread linked to item/booking
- Email notifications for new messages

### 6. Wishlist / Favorites
- Renters can save items to wishlist
- View all favorited items in one place
- Get notified when favorited items become available

## DocType Specifications

### Masters

#### Nirmaha Category
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| category_name | Data | Yes | Category name |
| parent_category | Link: Nirmaha Category | No | Parent for subcategories |
| image | Attach Image | No | Category image |
| description | Text | No | Category description |

#### Nirmaha Settings (Single)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| platform_name | Data | Yes | "Nirmaha" |
| platform_fee_percent | Percent | Yes | Default 10% |
| delivery_radius_miles | Int | Yes | Default 50 |
| min_deposit_percent | Percent | Yes | Minimum deposit % |
| stripe_publishable_key | Data | Yes | Stripe public key |
| stripe_secret_key | Password | Yes | Stripe secret key |
| default_currency | Link: Currency | Yes | USD |

### Listings

#### Nirmaha Lister
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| user | Link: User | Yes | Linked user account |
| lister_name | Data | Yes | Display name |
| phone | Data | Yes | Contact phone |
| email | Data | Yes | Contact email |
| address | Text | Yes | Full address |
| city | Data | Yes | City |
| state | Data | Yes | State |
| zip_code | Data | Yes | ZIP code |
| latitude | Float | No | Geo coordinate |
| longitude | Float | No | Geo coordinate |
| bio | Text | No | About the lister |
| profile_image | Attach Image | No | Profile photo |
| is_owner | Check | No | Platform owner (Shilpa) - no fees |
| stripe_account_id | Data | No | Stripe Connect account |
| total_listings | Int | No | Count (auto) |
| total_earnings | Currency | No | Lifetime earnings (auto) |
| rating | Float | No | Average rating (auto) |

#### Nirmaha Item
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| item_name | Data | Yes | Display name |
| item_code | Data | Yes | Unique code (auto) |
| lister | Link: Nirmaha Lister | Yes | Who owns this item |
| category | Link: Nirmaha Category | Yes | Item category |
| status | Select | Yes | Available/Rented/Unavailable |
| description | Text Editor | Yes | Full description |
| daily_rate | Currency | Yes | Price per day |
| weekly_rate | Currency | No | Price per week (discount) |
| deposit_amount | Currency | Yes | Security deposit |
| quantity | Int | Yes | How many available |
| condition | Select | Yes | New/Like New/Good/Fair |
| location_city | Data | Yes | Item location city |
| location_state | Data | Yes | Item location state |
| location_zip | Data | Yes | Item location ZIP |
| latitude | Float | No | Geo coordinate |
| longitude | Float | No | Geo coordinate |
| images | Table: Nirmaha Item Image | Yes | Multiple images |
| how_to_video | Data | No | YouTube/video URL |
| tags | Table MultiSelect | No | Searchable tags |

#### Nirmaha Item Image (Child Table)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| image | Attach Image | Yes | Item photo |
| is_primary | Check | No | Main display image |
| caption | Data | No | Image caption |

### Transactions

#### Nirmaha Booking
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| booking_id | Data | Yes | Auto-generated |
| customer | Link: User | Yes | Who is renting |
| status | Select | Yes | Pending/Confirmed/Picked Up/Returned/Cancelled |
| booking_date | Date | Yes | When booked |
| start_date | Date | Yes | Rental start |
| end_date | Date | Yes | Rental end |
| items | Table: Nirmaha Booking Item | Yes | Items in this booking |
| delivery_type | Select | Yes | Pickup/Delivery |
| delivery_address | Text | No | If delivery |
| delivery_fee | Currency | No | Calculated delivery cost |
| subtotal | Currency | No | Items total |
| platform_fee | Currency | No | 10% of partner items |
| deposit_amount | Currency | No | Total deposit required |
| grand_total | Currency | No | Final amount |
| stripe_payment_intent | Data | No | Stripe reference |
| notes | Text | No | Special requests |

#### Nirmaha Booking Item (Child Table)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| item | Link: Nirmaha Item | Yes | Item being rented |
| lister | Link: Nirmaha Lister | Yes | Item owner (auto-filled) |
| quantity | Int | Yes | How many |
| daily_rate | Currency | Yes | Rate at time of booking |
| days | Int | Yes | Number of days |
| line_total | Currency | Yes | Calculated |

#### Nirmaha Payout
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| lister | Link: Nirmaha Lister | Yes | Who gets paid |
| period_start | Date | Yes | Payout period start |
| period_end | Date | Yes | Payout period end |
| gross_amount | Currency | Yes | Total before fees |
| platform_fee | Currency | Yes | 10% deducted |
| net_amount | Currency | Yes | Amount to pay |
| status | Select | Yes | Pending/Paid |
| stripe_transfer_id | Data | No | Stripe reference |
| paid_date | Date | No | When paid |

### Reviews

#### Nirmaha Review
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| booking | Link: Nirmaha Booking | Yes | Related booking |
| reviewer | Link: User | Yes | Who wrote review |
| reviewee_type | Select | Yes | Item/Lister/Renter |
| item | Link: Nirmaha Item | No | If reviewing item |
| lister | Link: Nirmaha Lister | No | If reviewing lister |
| rating | Int | Yes | 1-5 stars |
| review_text | Text | No | Written review |

### Messaging

#### Nirmaha Conversation
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| conversation_id | Data | Yes | Auto-generated |
| item | Link: Nirmaha Item | No | Related item (if inquiry) |
| booking | Link: Nirmaha Booking | No | Related booking (if exists) |
| renter | Link: User | Yes | Customer in conversation |
| lister | Link: Nirmaha Lister | Yes | Lister in conversation |
| last_message_at | Datetime | No | For sorting |
| is_read_by_renter | Check | No | Renter read status |
| is_read_by_lister | Check | No | Lister read status |

#### Nirmaha Message (Child Table)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| sender | Link: User | Yes | Who sent message |
| message | Text | Yes | Message content |
| sent_at | Datetime | Yes | Timestamp |
| is_read | Check | No | Read status |

### Wishlist

#### Nirmaha Wishlist Item
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| user | Link: User | Yes | Who saved the item |
| item | Link: Nirmaha Item | Yes | Saved item |
| added_at | Datetime | Yes | When added |
| notify_available | Check | No | Notify when available |

## Workflows

### Booking Flow
```
Customer browses items
     ↓
Add to cart (multiple items, multiple listers)
     ↓
Select delivery/pickup
     ↓
Delivery cost calculated (if applicable)
     ↓
Deposit calculated (based on total value)
     ↓
Pay via Stripe (items + delivery + deposit)
     ↓
Booking confirmed → Notifications sent
     ↓
Pickup/Delivery on start date
     ↓
Return on end date
     ↓
Inspection
     ↓
├── No issues → Full deposit refund
└── Issues → Claim filed → Deposit adjusted
     ↓
Payout to listers (minus 10% platform fee)
```

### Lister Onboarding (Invite-Only)
```
Shilpa creates Nirmaha Lister account
     ↓
System sends invite email to lister
     ↓
Lister clicks link → Sets password
     ↓
Lister completes profile
     ↓
Lister connects Stripe account (Stripe Connect)
     ↓
Lister adds first listing
     ↓
Listing goes live
     ↓
Receive bookings → Fulfill → Get paid
```

## Delivery Cost Calculator

```python
def calculate_delivery_cost(origin_zip, destination_zip):
    """
    Calculate delivery fee based on distance.
    Uses ZIP code to estimate distance.
    """
    distance_miles = get_distance(origin_zip, destination_zip)

    if distance_miles > 50:
        return None  # Out of delivery range

    # Base fee + per-mile charge
    base_fee = 10.00
    per_mile = 0.50

    return base_fee + (distance_miles * per_mile)
```

## Platform Fee Logic

```python
def calculate_platform_fee(booking_items):
    """
    10% platform fee on ALL lister transactions.
    Only exception: Shilpa (is_owner=True) keeps 100%.
    """
    total_fee = 0

    for item in booking_items:
        if not item.lister.is_owner:
            total_fee += item.line_total * 0.10

    return total_fee
```

## Deposit Calculation

```python
def calculate_deposit(booking_items):
    """
    Deposit based on total order value.
    Minimum 20%, maximum 50% of item value.
    """
    total_value = sum(item.line_total for item in booking_items)

    # Tiered deposit
    if total_value < 100:
        return total_value * 0.50  # 50% for small orders
    elif total_value < 500:
        return total_value * 0.30  # 30% for medium
    else:
        return total_value * 0.20  # 20% for large orders
```

## Theme & Design

South Indian festive theme:
- **Colors**: Warm yellows, oranges, deep reds, gold accents
- **Patterns**: Rangoli-inspired borders, lotus motifs
- **Elements**: Banana leaf textures, traditional kolam patterns
- **Typography**: Clean modern fonts with decorative accents

## Stripe Integration

### Required Stripe Features
1. **Stripe Connect** - For multi-vendor payouts to listers
2. **Payment Intents** - For secure customer payments
3. **Refunds** - For deposit returns and cancellations
4. **Transfers** - For automated lister payouts

### Webhook Events
- `payment_intent.succeeded` - Mark booking as paid
- `payment_intent.payment_failed` - Handle failed payment
- `transfer.created` - Track lister payout
- `charge.refunded` - Track deposit refund

## Notifications

| Event | Channel | Recipient |
|-------|---------|-----------|
| New booking | Email + SMS | Lister |
| Booking confirmed | Email | Customer |
| Pickup reminder | Email + SMS | Customer |
| Return reminder | Email + SMS | Customer |
| Payout sent | Email | Lister |
| New review | Email | Lister |

## Reports

1. **Platform Dashboard**: Total bookings, revenue, active listings
2. **Lister Earnings**: Per-lister revenue and payouts
3. **Popular Items**: Most rented items
4. **Geographic Heat Map**: Rental activity by location
5. **Customer Analytics**: Repeat customers, average order value

## Future Enhancements

- Mobile app (React Native)
- Promotional codes / discounts
- Subscription plans for frequent renters
- Insurance integration for high-value items
