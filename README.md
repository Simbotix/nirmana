# Nirmaha

Peer-to-peer rental marketplace for props, party supplies, and event inventory. Built on [Frappe Framework](https://frappeframework.com) with a South Indian festive theme.

## Features

- **Multi-Vendor Marketplace**: Listers can add their own inventory, set prices, earn money
- **Beautiful Theme**: South Indian festive design (rangoli, lotuses, banana leaves)
- **Geotagging & Delivery**: Location-based search, delivery within 50-mile radius
- **Stripe Payments**: Secure payments with Stripe Connect for multi-vendor payouts
- **Platform Fees**: 10% fee on partner network listings
- **Refundable Deposits**: Calculated based on order value
- **DIY Videos**: Attach how-to videos to listings
- **Reviews & Ratings**: Customer reviews for items and listers

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
- `STRIPE_PUBLISHABLE_KEY` / `STRIPE_SECRET_KEY` - Payment gateway
- `STRIPE_CONNECT_CLIENT_ID` - Multi-vendor payouts
- `TWILIO_*` - SMS notifications (US market)
- `SITE_NAME` - Your Frappe site name

## Documentation

- [CLAUDE.md](./CLAUDE.md) - Development guidelines and project context
- [Frappe Framework Docs](https://frappeframework.com/docs)

## License

MIT License - see [LICENSE](./LICENSE)

## Author

Rajesh Medampudi ([@medampudi](https://github.com/medampudi))
Simbotix - [simbotix.com](https://simbotix.com)
