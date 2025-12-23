# CLAUDE.md - Nirmana

You are my ruthless mentor. Don't sugarcoat anything. If my idea is weak, call it trash and tell me why.

## Project Overview

**Nirmana** is a peer-to-peer rental marketplace for props, party supplies, and event inventory. Built on Frappe Framework with a South Indian festive theme.

| Attribute | Value |
|-----------|-------|
| **App Name** | nirmana |
| **Platform Type** | Peer-to-peer rental marketplace |
| **Owner** | Shilpa (Sister) |
| **IT Admin** | Rajesh |
| **Deadline** | March 2026 |
| **Theme** | South Indian festive (rangoli, lotuses, banana leaves) |
| **Target Market** | US-based (50-mile delivery radius) |
| **Payment Gateway** | Stripe |
| **Staging** | nirmana.press.appz.studio |

## Business Context

Shilpa runs a props and party supplies rental platform where:
- **Listers** (friends/peers) can add their own inventory for rent
- **Renters** browse and book items from multiple listers
- Platform takes **10% fee** on partner network listings
- Delivery available within **50-mile radius**
- Items include props, party supplies, decorations with DIY videos

This is a **family project** with a March deadline for community showcase.

## Core DocTypes

### Masters
| DocType | Purpose |
|---------|---------|
| `Nirmana Category` | Item categories (Props, Party Supplies, Decorations) |
| `Nirmana Settings` | Single DocType for app configuration |

### Listings
| DocType | Purpose |
|---------|---------|
| `Nirmana Lister` | Vendor/lister profiles with Stripe Connect |
| `Nirmana Item` | Rental items with images, pricing, location |
| `Nirmana Item Image` | Child table for multiple item images |

### Transactions
| DocType | Purpose |
|---------|---------|
| `Nirmana Booking` | Customer bookings (multi-item, multi-lister) |
| `Nirmana Booking Item` | Child table for items in booking |
| `Nirmana Payout` | Lister payouts (minus 10% platform fee) |

### Reviews
| DocType | Purpose |
|---------|---------|
| `Nirmana Review` | Customer reviews for items/listers |

### Messaging
| DocType | Purpose |
|---------|---------|
| `Nirmana Conversation` | Message thread between renter and lister |
| `Nirmana Message` | Individual messages (child table) |

### Wishlist
| DocType | Purpose |
|---------|---------|
| `Nirmana Wishlist Item` | Saved/favorited items per user |

## Platform Fee Logic

```python
# 10% platform fee on ALL lister transactions
# Only Shilpa (is_owner=True) keeps 100%
if not item.lister.is_owner:
    platform_fee = item.line_total * 0.10
```

## Key Features

### 1. Multi-Vendor Marketplace
- **Invite-only listers** - only Shilpa can create lister accounts
- Each lister has their own profile/storefront
- **10% platform fee on ALL lister transactions** (except Shilpa)
- All listers coordinate with Shilpa
- Listers set their own prices

### 2. Geotagging & Delivery
- Location info on all listings
- Delivery within 50-mile radius
- Delivery cost calculator (base fee + per-mile)
- Pickup option available

### 3. Customer Portal
- Browse items by category/location
- Multi-item cart (from different listers)
- Stripe payments (items + delivery + deposit)
- Order history and reviews

### 4. Lister Dashboard
- Manage listings
- View bookings and earnings
- Connect Stripe account for payouts
- See reviews

### 5. In-App Messaging
- Renters message listers about items
- Message threads linked to items/bookings
- Email notifications for new messages

### 6. Wishlist / Favorites
- Save items to wishlist
- Notify when favorited items become available

## Tech Stack

- **Backend**: Frappe Framework (Python)
- **Frontend**: Frappe UI + Custom web pages (South Indian theme)
- **Database**: MariaDB
- **Payments**: Stripe (Connect for multi-vendor payouts)
- **Geolocation**: ZIP code based distance calculation
- **Notifications**: Email + SMS

## Development Setup

### Prerequisites
- Frappe Bench installed
- Python 3.10+
- Node.js 18+
- MariaDB 10.6+

### Local Development
```bash
# Clone into bench apps folder
cd ~/frappe-bench/apps
git clone https://github.com/Simbotix/nirmana.git

# Install app
cd ~/frappe-bench
bench get-app nirmana
bench --site your-site.localhost install-app nirmana

# Start development
bench start
```

### Using Codespaces
1. Open repo in GitHub Codespaces
2. Devcontainer auto-configures Frappe environment
3. Run `bench start` to begin development

## Environment Variables

Copy `.env.example` to `.env` and configure:

```bash
# Stripe (Payments + Connect)
STRIPE_PUBLISHABLE_KEY=
STRIPE_SECRET_KEY=
STRIPE_WEBHOOK_SECRET=

# SMS Provider (Twilio for US)
TWILIO_ACCOUNT_SID=
TWILIO_AUTH_TOKEN=
TWILIO_PHONE_NUMBER=

# Site Configuration
SITE_NAME=nirmana.localhost
ADMIN_PASSWORD=
```

## File Structure

```
nirmana/
├── nirmana/
│   ├── __init__.py
│   ├── hooks.py
│   ├── modules.txt
│   ├── patches.txt
│   ├── nirmana/                    # Module folder
│   │   ├── doctype/
│   │   │   ├── nirmana_category/
│   │   │   ├── nirmana_settings/
│   │   │   ├── nirmana_lister/
│   │   │   ├── nirmana_item/
│   │   │   ├── nirmana_booking/
│   │   │   ├── nirmana_payout/
│   │   │   ├── nirmana_review/
│   │   │   └── ...
│   │   └── report/
│   ├── api/                        # Whitelisted APIs
│   │   ├── __init__.py
│   │   ├── items.py
│   │   ├── booking.py
│   │   ├── stripe.py
│   │   └── delivery.py
│   ├── public/
│   │   ├── css/nirmana.css         # South Indian festive theme
│   │   └── js/nirmana.js
│   ├── templates/
│   │   ├── pages/                  # Portal pages
│   │   └── includes/
│   └── www/                        # Web pages (marketplace frontend)
├── requirements/                   # Requirements docs
│   ├── BUSINESS-REQUIREMENTS.md
│   ├── STAGING-SETUP.md
│   └── requirement-discussion.md
├── .devcontainer/
├── .env.example
├── CLAUDE.md
├── LICENSE
├── pyproject.toml
├── README.md
├── requirements.txt
└── setup.py
```

## Coding Standards

1. **DocType naming**: Prefix with `Nirmana ` (e.g., `Nirmana Item`)
2. **Field naming**: snake_case
3. **Python**: Follow Frappe conventions, use type hints
4. **JavaScript**: Use Frappe's JS patterns
5. **CSS**: South Indian festive theme (warm colors, rangoli patterns)
6. **Tests**: Write tests for critical business logic

## API Endpoints

```python
# Search items by location/category
@frappe.whitelist(allow_guest=True)
def search_items(category=None, zip_code=None, radius=50):
    pass

# Check item availability for dates
@frappe.whitelist(allow_guest=True)
def check_availability(item_id, start_date, end_date):
    pass

# Calculate delivery cost
@frappe.whitelist(allow_guest=True)
def calculate_delivery(origin_zip, destination_zip):
    pass

# Create booking with Stripe payment
@frappe.whitelist()
def create_booking(items, delivery_address, payment_method_id):
    pass

# Stripe webhook handler
@frappe.whitelist(allow_guest=True)
def stripe_webhook():
    pass

# Lister: Connect Stripe account
@frappe.whitelist()
def connect_stripe_account(lister_id):
    pass

# Lister: Get earnings/payouts
@frappe.whitelist()
def get_lister_earnings(lister_id):
    pass
```

## Key Workflows

### Booking Flow
1. Customer browses items, adds to cart
2. Selects delivery or pickup
3. Delivery cost calculated (if applicable)
4. Deposit calculated based on total value
5. Pays via Stripe (items + delivery + deposit)
6. Booking confirmed → Notifications sent
7. Pickup/delivery on start date
8. Return on end date
9. Inspection → Deposit refunded or adjusted
10. Payout to listers (minus 10% platform fee)

### Lister Onboarding (Invite-Only)
1. Shilpa creates Nirmana Lister account
2. System sends invite email to lister
3. Lister clicks link → Sets password
4. Lister completes profile + connects Stripe
5. Add first listing → Goes live
6. Receive bookings → Fulfill → Get paid

## ClickUp Integration

Tasks tracked in ClickUp under:
- **Space**: Simbotix 10₿
- **Folder**: 🚀 Family Products MVP Sprint
- **List**: RentalOS - Sister ⚠️ MARCH DEADLINE

## Milestones

- [ ] Complete core DocTypes (Category, Settings, Lister, Item)
- [ ] Build item listing and search
- [ ] Build customer booking flow
- [ ] Integrate Stripe payments
- [ ] Integrate Stripe Connect for lister payouts
- [ ] Build lister dashboard
- [ ] Implement delivery cost calculator
- [ ] Build South Indian festive theme (CSS)
- [ ] Testing and pilot deployment
- [ ] Community showcase (March 2026)

## Developer

- **Name**: Rajesh Medampudi
- **Email**: rajesh@simbotix.com
- **Company**: Simbotix (One Person Company)
