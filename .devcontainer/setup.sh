#!/bin/bash
set -e

echo "🚀 Setting up Nirmaha development environment..."

# Navigate to bench directory
cd /home/frappe/frappe-bench

# Install the app from mounted workspace
echo "📦 Installing nirmaha app..."
bench get-app /workspace/apps/nirmaha --skip-assets

# Create a new site if it doesn't exist
SITE_NAME="nirmaha.localhost"
if [ ! -d "sites/$SITE_NAME" ]; then
    echo "🌐 Creating site: $SITE_NAME..."
    bench new-site $SITE_NAME \
        --mariadb-root-password root \
        --admin-password admin \
        --no-mariadb-socket
fi

# Install app on site
echo "📲 Installing nirmaha on $SITE_NAME..."
bench --site $SITE_NAME install-app nirmaha || true

# Set as default site
bench use $SITE_NAME

# Enable developer mode
bench --site $SITE_NAME set-config developer_mode 1

echo "✅ Setup complete!"
echo ""
echo "To start development:"
echo "  cd /home/frappe/frappe-bench"
echo "  bench start"
echo ""
echo "Access the site at: http://localhost:8000"
echo "Login: Administrator / admin"
