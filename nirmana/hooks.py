app_name = "nirmana"
app_title = "Nirmana"
app_publisher = "Simbotix"
app_description = "Peer-to-peer rental marketplace for props, party supplies, and event inventory"
app_email = "rajesh@simbotix.com"
app_license = "MIT"
app_logo_url = "/assets/nirmana/images/logo.png"

# Apps
required_apps = ["frappe"]

# Includes in <head>
# ------------------
app_include_css = "/assets/nirmana/css/nirmana.css"
app_include_js = "/assets/nirmana/js/nirmana.js"

# Website includes
# web_include_css = "/assets/nirmana/css/nirmana-web.css"
# web_include_js = "/assets/nirmana/js/nirmana-web.js"

# Home Pages
# ----------
# home_page = "equipment"
# website_route_rules = [
# 	{"from_route": "/equipment", "to_route": "equipment"},
# 	{"from_route": "/book/<equipment_id>", "to_route": "book"},
# ]

# Generators
# ----------
# website_generators = ["Equipment Item"]

# Jinja
# ----------
# add methods and filters to jinja environment
# jinja = {
# 	"methods": "nirmana.utils.jinja_methods",
# 	"filters": "nirmana.utils.jinja_filters"
# }

# Installation
# ------------
# before_install = "nirmana.install.before_install"
# after_install = "nirmana.install.after_install"

# Uninstallation
# ------------
# before_uninstall = "nirmana.uninstall.before_uninstall"
# after_uninstall = "nirmana.uninstall.after_uninstall"

# Integration Setup
# ------------------
# before_app_install = "nirmana.utils.before_app_install"
# after_app_install = "nirmana.utils.after_app_install"

# Desk Notifications
# ------------------
# notification_config = "nirmana.notifications.get_notification_config"

# Permissions
# -----------
# permission_query_conditions = {
# 	"Rental Booking": "nirmana.permissions.get_booking_permission_query_conditions",
# }
# has_permission = {
# 	"Rental Booking": "nirmana.permissions.has_booking_permission",
# }

# DocType Class
# ---------------
# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# doc_events = {
# 	"Rental Booking": {
# 		"on_submit": "nirmana.handlers.on_booking_submit",
# 		"on_cancel": "nirmana.handlers.on_booking_cancel",
# 	}
# }

# Scheduled Tasks
# ---------------
# scheduler_events = {
# 	"daily": [
# 		"nirmana.tasks.send_return_reminders"
# 	],
# 	"hourly": [
# 		"nirmana.tasks.check_overdue_rentals"
# 	],
# }

# Testing
# -------
# before_tests = "nirmana.install.before_tests"

# Overriding Methods
# ------------------------------
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "nirmana.event.get_events"
# }

# Exempt DocTypes from Fixtures
# -----------------------------
# fixtures = [
#     {"dt": "Custom Field", "filters": [["module", "=", "Nirmana"]]},
#     {"dt": "Property Setter", "filters": [["module", "=", "Nirmana"]]},
# ]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------
# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["nirmana.utils.before_request"]
# after_request = ["nirmana.utils.after_request"]

# Override REST API responses
# override_response = {
# 	"frappe.desk.desktop.get_workspace_sidebar_items": "nirmana.api.get_sidebar"
# }

# User Data Protection
# --------------------
user_data_fields = [
    {
        "doctype": "{doctype_1}",
        "filter_by": "{filter_by}",
        "redact_fields": ["{field_1}", "{field_2}"],
        "partial": 1,
    },
]

# Authentication and authorization
# --------------------------------
# auth_hooks = [
# 	"nirmana.auth.validate"
# ]
