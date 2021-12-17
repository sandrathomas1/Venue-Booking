// Copyright (c) 2021, sandra thomas and contributors
// For license information, please see license.txt

frappe.ui.form.on('Venue Booking', {
	refresh: function(frm, cdt , cdn) {
        frm.add_custom_button('Create Customer', () => {
            frappe.new_doc('Customer', {
                venue_booking: frm.doc.name
            })
        })
        frm.add_custom_button('Create Venue', () => {
            frappe.new_doc('Venue', {
                venue_booking: frm.doc.name
            })
        })
        //frm.add_custom_button('Venue Data', () => {
        //   frappe.new_doc('Venue Data', {
        //        venue_booking: frm.doc.name
          //  })
        //})
        var d = locals[cdt][cdn];
        frappe.model.set_value(cdt, cdn, "total_days", frappe.datetime.get_day_diff( d.to_date , d.from_date));
        refresh_field("total_days");
    },
}); 
frappe.ui.form.on('Sales Order Item',{ qty:function(frm, cdt, cdn) {
    var d = locals[cdt][cdn];
    var grand_total = 0.0;
    var total = 0.0;
    frappe.model.set_value(cdt, cdn, "total", d.rate * d.qty);
    frm.doc.menu.forEach(function(d) { grand_total +=d.total;});
    frm.set_value('grand_total',grand_total);
    refresh_field("total");
    
}
});

