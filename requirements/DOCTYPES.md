# Nirmana - DocType Specifications

Complete field-level specifications for all DocTypes in the Nirmana rental marketplace.

## Overview

| Category | DocTypes |
|----------|----------|
| **Masters** | Category, Settings |
| **Listings** | Lister, Item, Item Image |
| **Transactions** | Booking, Booking Item, Payout |
| **Reviews** | Review |
| **Messaging** | Conversation, Message |
| **Wishlist** | Wishlist Item |

---

## Masters

### Nirmana Category

Item categories (Props, Party Supplies, Decorations, etc.)

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| category_name | Data | Yes | Category name |
| parent_category | Link: Nirmana Category | No | Parent for subcategories |
| image | Attach Image | No | Category image |
| description | Text | No | Category description |

---

### Nirmana Settings (Single DocType)

Platform-wide configuration. Only one record exists.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| platform_name | Data | Yes | "Nirmana" |
| platform_fee_percent | Percent | Yes | Default: 10% |
| delivery_radius_miles | Int | Yes | Default: 50 |
| min_deposit_percent | Percent | Yes | Minimum deposit % |
| stripe_publishable_key | Data | Yes | Stripe public key |
| stripe_secret_key | Password | Yes | Stripe secret key |
| stripe_webhook_secret | Password | No | Stripe webhook secret |
| stripe_connect_client_id | Data | No | For lister payouts |
| default_currency | Link: Currency | Yes | USD |
| owner_lister | Link: Nirmana Lister | No | Shilpa's lister account (no fees) |

---

## Listings

### Nirmana Lister

Vendor/lister profiles. Created by site owner (invite-only).

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| **Basic Info** |
| user | Link: User | Yes | Linked user account |
| lister_name | Data | Yes | Display name |
| phone | Data | Yes | Contact phone |
| email | Data | Yes | Contact email |
| **Location** |
| address | Text | Yes | Full address |
| city | Data | Yes | City |
| state | Data | Yes | State |
| zip_code | Data | Yes | ZIP code |
| latitude | Float | No | Geo coordinate (auto from ZIP) |
| longitude | Float | No | Geo coordinate (auto from ZIP) |
| **Profile** |
| bio | Text | No | About the lister |
| profile_image | Attach Image | No | Profile photo |
| **Settings** |
| is_owner | Check | No | Platform owner (Shilpa) - no fees |
| stripe_account_id | Data | No | Stripe Connect account ID |
| stripe_onboarding_complete | Check | No | Stripe setup done? |
| **Stats (Auto-calculated)** |
| total_listings | Int | No | Count of active listings |
| total_earnings | Currency | No | Lifetime earnings |
| rating | Float | No | Average rating (1-5) |
| total_reviews | Int | No | Number of reviews |

---

### Nirmana Item

Rental items listed by listers.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| **Basic Info** |
| item_name | Data | Yes | Display name |
| item_code | Data | Yes | Unique code (auto-generated) |
| lister | Link: Nirmana Lister | Yes | Who owns this item |
| category | Link: Nirmana Category | Yes | Item category |
| status | Select | Yes | Available / Rented / Unavailable |
| **Description** |
| description | Text Editor | Yes | Full description |
| condition | Select | Yes | New / Like New / Good / Fair |
| quantity | Int | Yes | How many available (default: 1) |
| **Pricing** |
| daily_rate | Currency | Yes | Price per day |
| weekly_rate | Currency | No | Price per week (discount) |
| deposit_amount | Currency | Yes | Security deposit required |
| **Location** |
| location_city | Data | Yes | Item location city |
| location_state | Data | Yes | Item location state |
| location_zip | Data | Yes | Item location ZIP |
| latitude | Float | No | Geo coordinate |
| longitude | Float | No | Geo coordinate |
| **Media** |
| images | Table: Nirmana Item Image | Yes | Multiple images |
| how_to_video | Data | No | YouTube/video URL |
| **Tags** |
| tags | Table MultiSelect | No | Searchable tags |
| **Stats (Auto-calculated)** |
| total_bookings | Int | No | Times rented |
| avg_rating | Float | No | Average rating |

---

### Nirmana Item Image (Child Table)

Multiple images per item.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| image | Attach Image | Yes | Item photo |
| is_primary | Check | No | Main display image |
| caption | Data | No | Image caption |

---

## Transactions

### Nirmana Booking

Customer bookings. Can include multiple items from different listers.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| **Identification** |
| booking_id | Data | Yes | Auto-generated (NB-XXXXX) |
| customer | Link: User | Yes | Who is renting |
| status | Select | Yes | Pending / Confirmed / Picked Up / Returned / Cancelled |
| **Dates** |
| booking_date | Date | Yes | When booked |
| start_date | Date | Yes | Rental start |
| end_date | Date | Yes | Rental end |
| **Items** |
| items | Table: Nirmana Booking Item | Yes | Items in this booking |
| **Delivery** |
| delivery_type | Select | Yes | Pickup / Delivery |
| delivery_address | Text | No | If delivery selected |
| delivery_zip | Data | No | For cost calculation |
| delivery_fee | Currency | No | Calculated delivery cost |
| **Pricing** |
| subtotal | Currency | No | Items total (auto) |
| platform_fee | Currency | No | 10% of non-owner items (auto) |
| deposit_amount | Currency | No | Total deposit required (auto) |
| grand_total | Currency | No | Final amount (auto) |
| **Payment** |
| stripe_payment_intent | Data | No | Stripe reference |
| payment_status | Select | No | Pending / Paid / Refunded |
| paid_at | Datetime | No | Payment timestamp |
| **Deposit Refund** |
| deposit_refunded | Currency | No | Amount refunded |
| deposit_refund_date | Date | No | When refunded |
| deposit_notes | Text | No | Refund notes (if partial) |
| **Other** |
| notes | Text | No | Special requests |

---

### Nirmana Booking Item (Child Table)

Individual items within a booking.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| item | Link: Nirmana Item | Yes | Item being rented |
| lister | Link: Nirmana Lister | Yes | Item owner (auto-filled) |
| quantity | Int | Yes | How many |
| daily_rate | Currency | Yes | Rate at time of booking |
| days | Int | Yes | Number of days |
| line_total | Currency | Yes | quantity × daily_rate × days |

---

### Nirmana Payout

Payouts to listers after successful rentals.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| lister | Link: Nirmana Lister | Yes | Who gets paid |
| period_start | Date | Yes | Payout period start |
| period_end | Date | Yes | Payout period end |
| **Amounts** |
| gross_amount | Currency | Yes | Total before fees |
| platform_fee | Currency | Yes | 10% deducted |
| net_amount | Currency | Yes | Amount to pay (gross - fee) |
| **Status** |
| status | Select | Yes | Pending / Processing / Paid / Failed |
| stripe_transfer_id | Data | No | Stripe reference |
| paid_date | Date | No | When paid |
| failure_reason | Text | No | If failed |
| **Linked Bookings** |
| bookings | Table: Nirmana Payout Booking | No | Bookings included |

---

## Reviews

### Nirmana Review

Customer reviews for items and listers.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| booking | Link: Nirmana Booking | Yes | Related booking |
| reviewer | Link: User | Yes | Who wrote review |
| **Review Target** |
| reviewee_type | Select | Yes | Item / Lister |
| item | Link: Nirmana Item | No | If reviewing item |
| lister | Link: Nirmana Lister | No | If reviewing lister |
| **Review Content** |
| rating | Int | Yes | 1-5 stars |
| review_text | Text | No | Written review |
| **Timestamps** |
| reviewed_at | Datetime | Yes | When submitted |

---

## Messaging

### Nirmana Conversation

Message thread between a renter and lister.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| conversation_id | Data | Yes | Auto-generated |
| **Participants** |
| renter | Link: User | Yes | Customer in conversation |
| lister | Link: Nirmana Lister | Yes | Lister in conversation |
| **Context** |
| item | Link: Nirmana Item | No | Related item (if inquiry) |
| booking | Link: Nirmana Booking | No | Related booking (if exists) |
| **Messages** |
| messages | Table: Nirmana Message | No | Message history |
| **Status** |
| last_message_at | Datetime | No | For sorting |
| last_message_by | Link: User | No | Who sent last |
| is_read_by_renter | Check | No | Renter read status |
| is_read_by_lister | Check | No | Lister read status |

---

### Nirmana Message (Child Table)

Individual messages within a conversation.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| sender | Link: User | Yes | Who sent message |
| message | Text | Yes | Message content |
| sent_at | Datetime | Yes | Timestamp |
| is_read | Check | No | Read by recipient |

---

## Wishlist

### Nirmana Wishlist Item

Items saved/favorited by users.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| user | Link: User | Yes | Who saved the item |
| item | Link: Nirmana Item | Yes | Saved item |
| added_at | Datetime | Yes | When added |
| notify_available | Check | No | Notify when item becomes available |

---

## Field Type Reference

| Type | Description |
|------|-------------|
| Data | Single line text |
| Text | Multi-line text |
| Text Editor | Rich text with formatting |
| Int | Integer number |
| Float | Decimal number |
| Currency | Money (respects currency settings) |
| Percent | Percentage (0-100) |
| Check | Boolean (Yes/No) |
| Select | Dropdown with options |
| Link | Reference to another DocType |
| Table | Child table (one-to-many) |
| Table MultiSelect | Many-to-many via link |
| Date | Date only |
| Datetime | Date and time |
| Attach Image | Image upload |
| Password | Encrypted field |

---

## Status Options

### Nirmana Item.status
- Available
- Rented
- Unavailable

### Nirmana Booking.status
- Pending
- Confirmed
- Picked Up
- Returned
- Cancelled

### Nirmana Payout.status
- Pending
- Processing
- Paid
- Failed

### Nirmana Item.condition
- New
- Like New
- Good
- Fair

### Nirmana Booking.delivery_type
- Pickup
- Delivery

### Nirmana Review.reviewee_type
- Item
- Lister
