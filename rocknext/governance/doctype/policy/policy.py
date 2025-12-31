# Copyright (c) 2023, matbrgz and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _

class Policy(Document):
	def validate(self):
		if self.effective_date and self.expiration_date:
			if self.expiration_date < self.effective_date:
				frappe.throw(_("Expiration Date cannot be before Effective Date"))
