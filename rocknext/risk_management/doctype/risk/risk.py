# Copyright (c) 2023, matbrgz and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Risk(Document):
	def validate(self):
		self.calculate_risk_score()

	def calculate_risk_score(self):
		mapping = {
			"Low": 1,
			"Medium": 2,
			"High": 3
		}

		probability_score = mapping.get(self.probability, 0)
		impact_score = mapping.get(self.impact, 0)

		self.risk_score = probability_score * impact_score
