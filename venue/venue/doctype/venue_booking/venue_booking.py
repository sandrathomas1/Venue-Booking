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
