# CLAUDE.md - Nirmaha

You are my ruthless mentor. Don't sugarcoat anything. If my idea is weak, call it trash and tell me why.

## Project Overview

**Nirmaha** is an equipment rental management system built on Frappe Framework for my sister's rental business.

| Attribute | Value |
|-----------|-------|
| **App Name** | nirmaha |
| **Client** | Sister (Family Project) |
| **Deadline** | March 2025 |
| **Priority** | HIGH - Community showcase |
| **Staging** | nirmaha.press.appz.studio |
| **Production** | TBD |

## Business Context

Sister runs an equipment rental business and needs a system to:
- Track equipment inventory with QR codes
- Manage customer bookings and reservations
- Calculate rental pricing (hourly/daily/weekly/monthly)
- Handle deposits and damage reports
- Generate rental agreements and invoices
- SMS notifications for pickups/returns/overdue

This is a **family project** with a March deadline for community showcase.

## Core DocTypes

### Masters
| DocType | Purpose |
|---------|---------|
| `Rental Category` | Equipment categories (Electronics, Furniture, Tools, etc.) |
| `Rental Location` | Warehouse/store locations |
| `Rental Settings` | Single DocType for app configuration |

### Transactions
| DocType | Purpose |
|---------|---------|
| `Rental Equipment` | Equipment inventory with rates, images, QR codes |
| `Rental Customer` | Customer profiles linked to User |
| `Rental Booking` | Reservation/booking before pickup |
| `Rental Checkout` | When equipment leaves warehouse |
| `Rental Return` | When equipment comes back |
| `Rental Invoice` | Billing document |
| `Rental Deposit` | Security deposits |
| `Rental Damage Report` | Damage documentation |
| `Rental Maintenance` | Equipment maintenance records |
| `Rental Agreement` | Legal agreement PDF |

### Child Tables
| DocType | Purpose |
|---------|---------|
| `Rental Rate` | Pricing tiers (hourly/daily/weekly/monthly) |

## Pricing Engine

Equipment can have multiple rate types:
```
Hourly Rate: Rs X/hour (min 2 hours)
Daily Rate: Rs Y/day
Weekly Rate: Rs Z/week (7 days)
Monthly Rate: Rs W/month (30 days)
```

Auto-calculate best rate for customer based on duration.

## Key Features

### 1. Equipment Management
- QR code on each equipment item
- Status tracking: Available, Rented, Maintenance, Retired
- Photo documentation
- Depreciation tracking
- Maintenance scheduling

### 2. Customer Portal
- Browse equipment catalog
- Check availability calendar
- Make reservations
- View rental history
- Pay deposits/invoices via Razorpay

### 3. Operations Dashboard
- Today's pickups and returns
- Overdue rentals (red alerts)
- Equipment needing maintenance
- Revenue summary

### 4. Notifications
- SMS: Booking confirmation, pickup reminder, return reminder, overdue alert
- Email: Invoice, agreement PDF, payment confirmation

## Tech Stack

- **Backend**: Frappe Framework (Python)
- **Frontend**: Frappe UI (Vue.js components)
- **Database**: MariaDB
- **Payments**: Razorpay
- **SMS**: MSG91 or similar
- **QR Codes**: Python qrcode library
- **PDF**: Frappe print formats

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
git clone https://github.com/Simbotix/nirmaha.git

# Install app
cd ~/frappe-bench
bench get-app nirmaha
bench --site your-site.localhost install-app nirmaha

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
# Razorpay (Payments)
RAZORPAY_KEY_ID=
RAZORPAY_KEY_SECRET=

# SMS Provider
SMS_API_KEY=
SMS_SENDER_ID=

# Site Configuration
SITE_NAME=nirmaha.localhost
ADMIN_PASSWORD=
```

## File Structure

```
nirmaha/
├── nirmaha/
│   ├── __init__.py
│   ├── hooks.py
│   ├── modules.txt
│   ├── patches.txt
│   ├── nirmaha/                    # Module folder
│   │   ├── doctype/
│   │   │   ├── rental_equipment/
│   │   │   ├── rental_customer/
│   │   │   ├── rental_booking/
│   │   │   ├── rental_checkout/
│   │   │   ├── rental_return/
│   │   │   ├── rental_invoice/
│   │   │   └── ...
│   │   └── report/
│   ├── api/                        # Whitelisted APIs
│   │   ├── __init__.py
│   │   ├── equipment.py
│   │   ├── booking.py
│   │   └── payments.py
│   ├── public/
│   │   ├── css/nirmaha.css
│   │   └── js/nirmaha.js
│   ├── templates/
│   │   ├── pages/                  # Portal pages
│   │   └── includes/
│   └── www/                        # Web pages
├── .devcontainer/
├── .github/workflows/
├── .env.example
├── CLAUDE.md
├── LICENSE
├── pyproject.toml
├── README.md
├── requirements.txt
└── setup.py
```

## Coding Standards

1. **DocType naming**: Prefix with `Rental ` (e.g., `Rental Equipment`)
2. **Field naming**: snake_case
3. **Python**: Follow Frappe conventions, use type hints
4. **JavaScript**: Use Frappe's JS patterns
5. **Tests**: Write tests for critical business logic

## API Endpoints

```python
# Check equipment availability
@frappe.whitelist()
def check_equipment_availability(equipment_id, start_date, end_date):
    pass

# Create booking from portal
@frappe.whitelist(allow_guest=True)
def create_booking(equipment_id, customer_details, start_date, end_date):
    pass

# Process Razorpay payment
@frappe.whitelist()
def process_payment(booking_id, payment_id):
    pass

# Generate equipment QR code
@frappe.whitelist()
def get_equipment_qr(equipment_id):
    pass
```

## Key Workflows

### Booking → Checkout → Return Flow
1. Customer creates `Rental Booking` (status: Reserved)
2. Staff confirms and collects deposit → `Rental Deposit`
3. Equipment handed over → `Rental Checkout` created
4. Equipment returned → `Rental Return` created
5. Inspection done → `Rental Damage Report` if needed
6. Invoice generated → `Rental Invoice`
7. Deposit refunded/adjusted

## ClickUp Integration

Tasks tracked in ClickUp under:
- **Space**: Simbotix 10₿
- **Folder**: 🚀 Family Products MVP Sprint
- **List**: RentalOS - Sister ⚠️ MARCH DEADLINE

## Milestones

- [ ] Create estimate document for sister
- [ ] Send estimate and get approval
- [ ] Complete core DocTypes
- [ ] Build Operations Dashboard
- [ ] Build Customer Portal
- [ ] Integrate Razorpay
- [ ] Implement SMS notifications
- [ ] Testing and pilot deployment
- [ ] Community showcase (March)

## Developer

- **Name**: Rajesh Medampudi
- **Email**: rajesh@simbotix.com
- **Company**: Simbotix (One Person Company)
