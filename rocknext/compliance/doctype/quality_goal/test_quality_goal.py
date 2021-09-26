# -*- coding: utf-8 -*-
# Copyright (c) 2018, Frappe and Contributors
# See license.txt
from __future__ import unicode_literals

import unittest

import frappe


class TestComplianceGoal(unittest.TestCase):
	def test_compliance_goal(self):
		# no code, just a basic sanity check
		goal = get_compliance_goal()
		self.assertTrue(goal)
		goal.delete()

def get_compliance_goal():
	return frappe.get_doc(dict(
		doctype = 'Compliance Goal',
		goal = 'Test Compliance Module',
		frequency = 'Daily',
		objectives = [
			dict(objective = 'Check test cases', target='100', uom='Percent')
		]
	)).insert()
