#!/usr/bin/env python

import unittest

from math_trees import math_trees


class TestMathTrees(unittest.TestCase):
    def test_basic_string(self):
        math_string = "3 + 4 * 2"
        # self.assertEqual(value, 8)

    def test_another_string(self):
        math_string = "8 - 9 / 3"
        # self.assertEqual(value, 5)
