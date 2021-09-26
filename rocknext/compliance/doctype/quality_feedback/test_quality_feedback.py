# -*- coding: utf-8 -*-
# Copyright (c) 2019, Frappe Technologies Pvt. Ltd. and Contributors
# See license.txt
from __future__ import unicode_literals

import unittest

import frappe


class TestComplianceFeedback(unittest.TestCase):
	def test_compliance_feedback(self):
		template = frappe.get_doc(dict(
			doctype = 'Compliance Feedback Template',
			template = 'Test Template',
			parameters = [
				dict(parameter='Test Parameter 1'),
				dict(parameter='Test Parameter 2')
			]
		)).insert()

		feedback = frappe.get_doc(dict(
			doctype = 'Compliance Feedback',
			template = template.name,
			document_type = 'User',
			document_name = frappe.session.user
		)).insert()

		self.assertEqual(template.parameters[0].parameter, feedback.parameters[0].parameter)

		feedback.delete()
		template.delete()
