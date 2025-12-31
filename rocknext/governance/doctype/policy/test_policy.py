# Copyright (c) 2023, matbrgz and contributors
# For license information, please see license.txt

import frappe
from frappe.tests.utils import FrappeTestCase
from frappe.utils import add_days, today

class TestPolicy(FrappeTestCase):
	def test_expiration_date_validation(self):
		policy = frappe.new_doc("Policy")
		policy.title = "Test Policy"
		policy.effective_date = today()
		policy.expiration_date = add_days(today(), -1) # Yesterday

		self.assertRaises(frappe.ValidationError, policy.save)

		policy.expiration_date = add_days(today(), 1) # Tomorrow
		policy.save() # Should save successfully
