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

## Detailed Specifications

See separate documents for detailed specifications:

- **[DOCTYPES.md](./DOCTYPES.md)** - Complete field-level DocType specifications
- **[BUSINESS-LOGIC.md](./BUSINESS-LOGIC.md)** - Calculation logic, APIs, and workflows

### DocType Summary

| Category | DocTypes |
|----------|----------|
| **Masters** | Nirmaha Category, Nirmaha Settings |
| **Listings** | Nirmaha Lister, Nirmaha Item, Nirmaha Item Image |
| **Transactions** | Nirmaha Booking, Nirmaha Booking Item, Nirmaha Payout |
| **Reviews** | Nirmaha Review |
| **Messaging** | Nirmaha Conversation, Nirmaha Message |
| **Wishlist** | Nirmaha Wishlist Item |

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
