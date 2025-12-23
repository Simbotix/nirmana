# Nirmaha - Time Estimate

Estimated development time for the complete Nirmaha rental marketplace.

## Summary

| Phase | Hours | Description |
|-------|-------|-------------|
| Phase 1: Foundation | 40-50 | DocTypes, basic setup |
| Phase 2: Core Features | 60-80 | Booking, payments, lister dashboard |
| Phase 3: Customer Experience | 40-50 | Portal, messaging, wishlist |
| Phase 4: Polish & Launch | 30-40 | Theme, testing, deployment |
| **Total** | **170-220 hrs** | ~4-6 weeks full-time |

---

## Phase 1: Foundation (40-50 hours)

### DocTypes & Data Model (25-30 hrs)

| Task | Hours | Notes |
|------|-------|-------|
| Nirmaha Settings (Single) | 2 | Platform config |
| Nirmaha Category | 2 | With hierarchy |
| Nirmaha Lister | 4 | Profile, permissions, invite flow |
| Nirmaha Item + Item Image | 6 | Multi-image, geo-location |
| Nirmaha Booking + Booking Item | 6 | Complex with calculations |
| Nirmaha Payout | 3 | Lister payouts |
| Nirmaha Review | 2 | Rating system |

### Basic Setup (15-20 hrs)

| Task | Hours | Notes |
|------|-------|-------|
| App configuration | 2 | Hooks, permissions |
| User roles setup | 3 | Lister, Customer roles |
| Lister invite system | 4 | Email invite, password setup |
| ZIP code geo-lookup | 4 | Distance calculation |
| Basic API structure | 4 | API scaffolding |

---

## Phase 2: Core Features (60-80 hours)

### Stripe Integration (20-25 hrs)

| Task | Hours | Notes |
|------|-------|-------|
| Stripe payment setup | 6 | PaymentIntents, checkout |
| Stripe Connect (listers) | 8 | Onboarding, account linking |
| Webhook handlers | 4 | Payment events |
| Refund logic | 3 | Deposit refunds |
| Payout automation | 4 | Weekly lister payouts |

### Booking System (20-25 hrs)

| Task | Hours | Notes |
|------|-------|-------|
| Availability checking | 4 | Date overlap logic |
| Cart functionality | 6 | Multi-item, multi-lister |
| Delivery cost calculator | 4 | ZIP-based distance |
| Deposit calculation | 2 | Tiered logic |
| Platform fee calculation | 2 | Owner vs lister |
| Booking status workflow | 4 | State transitions |
| Booking APIs | 4 | Create, confirm, cancel |

### Lister Dashboard (20-30 hrs)

| Task | Hours | Notes |
|------|-------|-------|
| Dashboard page | 6 | Stats, recent activity |
| Listing management | 8 | CRUD for items |
| Booking management | 6 | View, confirm bookings |
| Earnings view | 4 | Revenue, payouts |
| Stripe Connect UI | 4 | Onboarding flow |

---

## Phase 3: Customer Experience (40-50 hours)

### Customer Portal (20-25 hrs)

| Task | Hours | Notes |
|------|-------|-------|
| Homepage / Browse | 6 | Category grid, search |
| Item detail page | 4 | Images, video, reviews |
| Search & filters | 6 | Location, category, price |
| Checkout flow | 6 | Multi-step, payment |
| Order history | 3 | Past bookings |

### Messaging System (10-12 hrs)

| Task | Hours | Notes |
|------|-------|-------|
| Conversation DocTypes | 2 | Already defined |
| Message APIs | 4 | Send, fetch, mark read |
| Inbox UI | 4 | Conversation list, thread view |
| Email notifications | 2 | New message alerts |

### Wishlist (6-8 hrs)

| Task | Hours | Notes |
|------|-------|-------|
| Wishlist DocType | 1 | Already defined |
| Add/remove APIs | 2 | Simple CRUD |
| Wishlist page | 2 | Grid of saved items |
| Availability notifications | 2 | Email when available |

### Reviews (5-6 hrs)

| Task | Hours | Notes |
|------|-------|-------|
| Review submission | 3 | After booking complete |
| Review display | 2 | On item/lister pages |

---

## Phase 4: Polish & Launch (30-40 hours)

### Theme & Design (15-20 hrs)

| Task | Hours | Notes |
|------|-------|-------|
| South Indian theme CSS | 8 | Colors, patterns, motifs |
| Responsive design | 4 | Mobile-friendly |
| Icons & illustrations | 4 | Rangoli, lotus elements |
| Print formats | 2 | Booking confirmation |

### Notifications (8-10 hrs)

| Task | Hours | Notes |
|------|-------|-------|
| Email templates | 4 | All notification types |
| Scheduled jobs | 2 | Reminders |
| Twilio SMS setup | 3 | Optional |

### Testing & Deployment (10-15 hrs)

| Task | Hours | Notes |
|------|-------|-------|
| Testing (manual) | 6 | All flows |
| Bug fixes | 4 | Buffer |
| Staging deployment | 2 | press.appz.studio |
| Production setup | 3 | DNS, SSL, go-live |

---

## Assumptions

1. **Single developer** working on this
2. **No major scope changes** during development
3. **Frappe/ERPNext experience** - familiar with framework
4. **Assets provided** - logos, images from Shilpa
5. **Stripe account ready** - with Connect enabled

## Risk Factors

| Risk | Impact | Mitigation |
|------|--------|------------|
| Stripe Connect complexity | +10-15 hrs | Use Stripe's hosted onboarding |
| Geo-location accuracy | +5-10 hrs | Use simple ZIP database |
| Theme iterations | +10-20 hrs | Get moodboard sign-off early |
| Scope creep | +20-40 hrs | Lock features before Phase 2 |

## Recommended Approach

### MVP First (100-120 hrs)
Ship with:
- Basic listings & booking
- Stripe payments (no Connect initially)
- Simple lister dashboard
- Basic theme

### Full Version (170-220 hrs)
Add:
- Stripe Connect payouts
- Messaging
- Wishlist
- Polished theme

---

## Cost Estimate

### Family Price (Fixed)

| Package | What's Included | Price |
|---------|-----------------|-------|
| **Full Platform** | Complete Nirmaha marketplace with all features | **₹2,00,000** |

This includes:
- All DocTypes and data model
- Complete booking system
- Stripe payments + Stripe Connect (lister payouts)
- Lister dashboard
- Customer portal
- Messaging system
- Wishlist / favorites
- South Indian festive theme
- Deployment to staging + production

### Payment Terms

| Milestone | Amount | When |
|-----------|--------|------|
| Project Start | ₹1,00,000 | Upfront |
| Delivery | ₹1,00,000 | On completion |

### What This Means

| Metric | Value |
|--------|-------|
| Estimated hours | 170-220 |
| Effective rate | ₹910-1,175/hr |
| Market rate | ₹5,810/hr |
| **Discount** | **~80% off** |

*This is family pricing. Not available for external clients.*

---

## Timeline Options

### Aggressive (Full-time)
- Phase 1: Week 1-2
- Phase 2: Week 2-4
- Phase 3: Week 4-5
- Phase 4: Week 5-6
- **Total: 6 weeks**

### Realistic (With buffer)
- Phase 1: Week 1-2
- Phase 2: Week 3-5
- Phase 3: Week 6-7
- Phase 4: Week 8
- **Total: 8 weeks**

### Part-time (20 hrs/week)
- **Total: 10-12 weeks**

---

*Deadline: March 2026 - Plenty of time for quality delivery.*
