# Copyright (c) 2021, sandra thomas and contributors
# For license information, please see license.txt
from __future__ import unicode_literals
import frappe
from frappe.website.website_generator import WebsiteGenerator

class VenueBooking(WebsiteGenerator):
	def before_save(self):
		exists = frappe.db.exists(
			"Venue Booking",
			{
				"venue":self.venue,
				"docstatus": 1,
				"to_date": (">", self.from_date),
			},
		)
		if exists:
			frappe.throw("The venue already Booked On That Day")
	#@frappe.whitelist()
	def before_submit(self):
		doc=frappe.get_doc({
		'doctype':"Venue Data",
		'customer':self.customer,
		'venue': self.venue,
		'from_date': self.from_date,
		'to_date': self.to_date
		})
		doc.insert()
		doc.submit()

		

