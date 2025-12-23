# Nirmaha

Equipment Rental Management System built on [Frappe Framework](https://frappeframework.com).

## Features

- **Equipment Inventory**: Track all rental equipment with QR codes, photos, and maintenance history
- **Customer Portal**: Self-service booking, availability checking, and payment
- **Flexible Pricing**: Hourly, daily, weekly, and monthly rates with automatic best-rate calculation
- **Booking Management**: Reservations, checkouts, returns, and damage reports
- **Deposit Handling**: Security deposit collection and refund tracking
- **Invoicing**: Automatic invoice generation with Razorpay integration
- **Notifications**: SMS and email alerts for pickups, returns, and overdue items
- **Reports**: Revenue, utilization, and inventory reports

## Quick Start

### Using GitHub Codespaces (Recommended)

1. Click **Code** → **Codespaces** → **Create codespace on main**
2. Wait for the container to build (~5 minutes first time)
3. Run `bench start` in the terminal
4. Open `http://localhost:8000` in browser
5. Login: `Administrator` / `admin`

### Local Development

```bash
# Prerequisites: Frappe Bench installed
cd ~/frappe-bench/apps
git clone https://github.com/Simbotix/nirmaha.git

cd ~/frappe-bench
bench get-app nirmaha
bench new-site nirmaha.localhost
bench --site nirmaha.localhost install-app nirmaha
bench --site nirmaha.localhost set-config developer_mode 1
bench use nirmaha.localhost
bench start
```

## Configuration

Copy `.env.example` to `.env` and configure:

```bash
cp .env.example .env
```

Key settings:
- `RAZORPAY_KEY_ID` / `RAZORPAY_KEY_SECRET` - Payment gateway
- `SMS_API_KEY` - SMS notifications
- `SITE_NAME` - Your Frappe site name

## Documentation

- [CLAUDE.md](./CLAUDE.md) - Development guidelines and project context
- [Frappe Framework Docs](https://frappeframework.com/docs)

## License

MIT License - see [LICENSE](./LICENSE)

## Author

Rajesh Medampudi ([@medampudi](https://github.com/medampudi))
Simbotix - [simbotix.com](https://simbotix.com)
