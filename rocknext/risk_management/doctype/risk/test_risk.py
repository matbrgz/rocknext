# Copyright (c) 2023, matbrgz and contributors
# For license information, please see license.txt

import frappe
from frappe.tests.utils import FrappeTestCase

class TestRisk(FrappeTestCase):
	def test_risk_score_calculation(self):
		risk = frappe.new_doc("Risk")
		risk.subject = "Test Risk"
		risk.risk_category = "Operational"
		risk.probability = "Low"
		risk.impact = "Low"
		risk.save()
		self.assertEqual(risk.risk_score, 1)

		risk.probability = "Medium"
		risk.impact = "Medium"
		risk.save()
		self.assertEqual(risk.risk_score, 4)

		risk.probability = "High"
		risk.impact = "High"
		risk.save()
		self.assertEqual(risk.risk_score, 9)

		risk.probability = "Low"
		risk.impact = "High"
		risk.save()
		self.assertEqual(risk.risk_score, 3)

		risk.probability = "High"
		risk.impact = "Medium"
		risk.save()
		self.assertEqual(risk.risk_score, 6)
