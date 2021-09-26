# -*- coding: utf-8 -*-
# Copyright (c) 2018, Frappe and Contributors
# See license.txt
from __future__ import unicode_literals

import unittest

import frappe

from ..compliance_goal.test_compliance_goal import get_compliance_goal
from .compliance_review import review


class TestComplianceReview(unittest.TestCase):
	def test_review_creation(self):
		compliance_goal = get_compliance_goal()
		review()

		# check if review exists
		compliance_review = frappe.get_doc('Compliance Review', dict(goal = compliance_goal.name))
		self.assertEqual(compliance_goal.objectives[0].target, compliance_review.reviews[0].target)
		compliance_review.delete()

		compliance_goal.delete()
