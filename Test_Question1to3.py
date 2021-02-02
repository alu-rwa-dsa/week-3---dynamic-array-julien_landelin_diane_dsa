# Question 1to3 - unit test

from Question1to3 import *

# Performing Unit Tests

import unittest


class TestQuestion1to3(unittest.TestCase):

    def test_len(self):
        test_array = array2([30, 78, 65, 43, 90, 87, 12, 24])
        self.assertEqual(test_array.len(), 8)

    def test_get(self):
        test_array = array2([30, 78, 65, 43, 90, 87, 12, 24])
        self.assertEqual(test_array.get(4), 90)
        self.assertEqual(test_array.get(2), 65)

    def test_set(self):
        test_array = array2([30, 78, 65, 43, 90, 87, 12, 24])
        self.assertEqual(test_array.set(5, 2), [30, 78, 5, 43, 90, 87, 12, 24])

    def test_add(self):
        test_array = array2([30, 78, 65, 43, 90, 87, 12, 24])
        self.assertEqual(test_array.add(36), [30, 78, 65, 43, 90, 87, 12, 24, 36])

    def test_dele(self):
        test_array = array2([30, 78, 65, 43, 90, 87, 12, 24])
        self.assertEqual(test_array.dele(), [30, 78, 65, 43, 90, 87, 12])

    def test_contains(self):
        test_array = array2([30, 78, 65, 43, 90, 87, 12, 24])
        self.assertEqual(contains(test_array, 30), True)
        self.assertEqual(contains(test_array, 8), False)

    def test_reverse(self):
        test_array = array2([30, 78, 65, 43, 90, 87, 12, 24])
        self.assertEqual(reverse(test_array), [24, 12, 87, 90, 43, 65, 78, 30])

    def test_insert(self):
        test_array = array2([30, 78, 65, 43, 90, 87, 12, 24])
        self.assertEqual(insert(test_array, 50, 4), [30, 78, 65, 43, 50, 90, 87, 12, 24])
