app_name = "nirmaha"
app_title = "Nirmaha"
app_publisher = "Simbotix"
app_description = "Equipment Rental Management System"
app_email = "rajesh@simbotix.com"
app_license = "MIT"
app_logo_url = "/assets/nirmaha/images/logo.png"

# Apps
required_apps = ["frappe"]

# Includes in <head>
# ------------------
app_include_css = "/assets/nirmaha/css/nirmaha.css"
app_include_js = "/assets/nirmaha/js/nirmaha.js"

# Website includes
# web_include_css = "/assets/nirmaha/css/nirmaha-web.css"
# web_include_js = "/assets/nirmaha/js/nirmaha-web.js"

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
# 	"methods": "nirmaha.utils.jinja_methods",
# 	"filters": "nirmaha.utils.jinja_filters"
# }

# Installation
# ------------
# before_install = "nirmaha.install.before_install"
# after_install = "nirmaha.install.after_install"

# Uninstallation
# ------------
# before_uninstall = "nirmaha.uninstall.before_uninstall"
# after_uninstall = "nirmaha.uninstall.after_uninstall"

# Integration Setup
# ------------------
# before_app_install = "nirmaha.utils.before_app_install"
# after_app_install = "nirmaha.utils.after_app_install"

# Desk Notifications
# ------------------
# notification_config = "nirmaha.notifications.get_notification_config"

# Permissions
# -----------
# permission_query_conditions = {
# 	"Rental Booking": "nirmaha.permissions.get_booking_permission_query_conditions",
# }
# has_permission = {
# 	"Rental Booking": "nirmaha.permissions.has_booking_permission",
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
# 		"on_submit": "nirmaha.handlers.on_booking_submit",
# 		"on_cancel": "nirmaha.handlers.on_booking_cancel",
# 	}
# }

# Scheduled Tasks
# ---------------
# scheduler_events = {
# 	"daily": [
# 		"nirmaha.tasks.send_return_reminders"
# 	],
# 	"hourly": [
# 		"nirmaha.tasks.check_overdue_rentals"
# 	],
# }

# Testing
# -------
# before_tests = "nirmaha.install.before_tests"

# Overriding Methods
# ------------------------------
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "nirmaha.event.get_events"
# }

# Exempt DocTypes from Fixtures
# -----------------------------
# fixtures = [
#     {"dt": "Custom Field", "filters": [["module", "=", "Nirmaha"]]},
#     {"dt": "Property Setter", "filters": [["module", "=", "Nirmaha"]]},
# ]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------
# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["nirmaha.utils.before_request"]
# after_request = ["nirmaha.utils.after_request"]

# Override REST API responses
# override_response = {
# 	"frappe.desk.desktop.get_workspace_sidebar_items": "nirmaha.api.get_sidebar"
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
# 	"nirmaha.auth.validate"
# ]
