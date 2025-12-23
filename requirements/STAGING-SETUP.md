# Staging Site Setup Instructions

## Site Details

| Property | Value |
|----------|-------|
| **Staging URL** | https://nirmana.press.appz.studio |
| **Press Dashboard** | https://press.appz.studio |
| **GitHub Repo** | https://github.com/Simbotix/nirmana |

## 1. Add App to Frappe Press

In press.appz.studio dashboard:

1. Go to **Apps** → **New App**
2. Fill in:
   - **App Name**: nirmana
   - **GitHub URL**: https://github.com/Simbotix/nirmana
   - **Branch**: main
3. Save and wait for app to be added

## 2. Create Site

1. Go to **Sites** → **New Site**
2. Configure:
   - **Subdomain**: nirmana
   - **Apps**: Select `frappe` + `nirmana`
   - **Plan**: Choose appropriate plan
3. Create site

## 3. Site Configuration

After site is created, add these to site_config.json via Press dashboard or SSH:

```json
{
  "razorpay_key_id": "rzp_live_RpdOex3j3a8AOE",
  "razorpay_key_secret": "STORED_IN_VAULT",
  "sms_provider": "msg91",
  "sms_api_key": "STORED_IN_VAULT",
  "sms_sender_id": "NIRMHA",
  "developer_mode": 0
}
```

## 4. Post-Deployment Setup

### Enable Scheduler
```bash
bench --site nirmana.press.appz.studio enable-scheduler
```

### Configure Razorpay
1. Login as Administrator
2. Go to: **Setup > Integrations > Razorpay Settings**
3. Enter API credentials
4. Set webhook URL: `https://nirmana.press.appz.studio/api/method/nirmana.api.payments.razorpay_webhook`

### Configure SMS
1. Go to: **Setup > SMS Settings** (or create custom doctype)
2. Enter MSG91 API key
3. Set sender ID: NIRMHA

## 5. Generate API Keys

For external integrations:

1. Login as Administrator
2. Go to: **Setup > Users > Administrator**
3. Scroll to **API Access**
4. Click **Generate Keys**
5. Store securely:

```bash
# Add to deployment_server/.env
NIRMAHA_STAGING_URL=https://nirmana.press.appz.studio
NIRMAHA_API_KEY=<generated_api_key>
NIRMAHA_API_SECRET=<generated_api_secret>
```

## 6. DNS Configuration

If using custom domain later:

| Type | Name | Value |
|------|------|-------|
| A | nirmana | 65.21.126.235 |
| CNAME | www.nirmana | nirmana.press.appz.studio |

## 7. SSL Certificate

Frappe Press handles SSL automatically via Let's Encrypt.

## Verification Checklist

- [ ] Site accessible at https://nirmana.press.appz.studio
- [ ] Can login as Administrator
- [ ] Nirmana app installed and visible in modules
- [ ] Razorpay integration configured
- [ ] SMS provider configured
- [ ] Scheduler enabled
- [ ] API keys generated and stored
