// Nirmaha - Equipment Rental Management System
// Main JavaScript file

frappe.provide("nirmaha");

nirmaha = {
    // Format currency for display
    format_currency: function(amount, currency) {
        currency = currency || frappe.defaults.get_default("currency");
        return format_currency(amount, currency);
    },

    // Calculate rental duration
    calculate_duration: function(start_date, end_date) {
        if (!start_date || !end_date) return 0;

        const start = frappe.datetime.str_to_obj(start_date);
        const end = frappe.datetime.str_to_obj(end_date);
        const diff = frappe.datetime.get_diff(end, start);

        return Math.max(1, diff + 1); // Minimum 1 day
    },

    // Calculate rental price
    calculate_rental_price: function(equipment, duration, rate_type) {
        rate_type = rate_type || "daily";

        let rate = 0;
        switch(rate_type) {
            case "hourly":
                rate = equipment.hourly_rate || 0;
                break;
            case "daily":
                rate = equipment.daily_rate || 0;
                break;
            case "weekly":
                rate = equipment.weekly_rate || 0;
                duration = Math.ceil(duration / 7);
                break;
            case "monthly":
                rate = equipment.monthly_rate || 0;
                duration = Math.ceil(duration / 30);
                break;
        }

        return rate * duration;
    },

    // Show equipment availability
    check_availability: function(equipment_id, start_date, end_date, callback) {
        frappe.call({
            method: "nirmaha.api.check_equipment_availability",
            args: {
                equipment_id: equipment_id,
                start_date: start_date,
                end_date: end_date
            },
            callback: function(r) {
                if (callback) callback(r.message);
            }
        });
    },

    // Generate QR code for equipment
    generate_qr_code: function(equipment_id, target_element) {
        frappe.call({
            method: "nirmaha.api.get_equipment_qr",
            args: { equipment_id: equipment_id },
            callback: function(r) {
                if (r.message && target_element) {
                    $(target_element).html(r.message);
                }
            }
        });
    }
};

// Extend Frappe's Desk
$(document).ready(function() {
    // Add quick actions if on Nirmaha workspace
    if (frappe.get_route()[0] === "Workspaces" &&
        frappe.get_route()[1] === "Nirmaha") {
        // Custom workspace initialization
    }
});
