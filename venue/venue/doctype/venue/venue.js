// Copyright (c) 2021, sandra thomas and contributors
// For license information, please see license.txt

frappe.ui.form.on('Venue', {
	refresh: function(frm) {
		rm.add_custom_button('Create Item', () => {
            frappe.new_doc('Items', {
                venue: frm.doc.name
            })
		})
		
	}
});
