#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_ordered_list(self):
        """Max is found in an already ordered list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Max is found in an unordered list."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_start(self):
        """Max is found when it's the first element."""
        self.assertEqual(max_integer([9, 1, 2, 3]), 9)

    def test_max_at_end(self):
        """Max is found when it's the last element."""
        self.assertEqual(max_integer([1, 2, 3, 9]), 9)

    def test_single_element(self):
        """Max of a single-element list is that element."""
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """Max of an empty list is None."""
        self.assertIsNone(max_integer([]))

    def test_no_argument(self):
        """Max with no argument defaults to an empty list, returns None."""
        self.assertIsNone(max_integer())

    def test_negative_numbers(self):
        """Max is found correctly among negative numbers."""
        self.assertEqual(max_integer([-1, -5, -3, -2]), -1)

    def test_mixed_positive_negative(self):
        """Max is found correctly among mixed positive/negative numbers."""
        self.assertEqual(max_integer([-10, 0, 5, -3, 8, 2]), 8)

    def test_duplicate_max_values(self):
        """Max is returned correctly when the max value repeats."""
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)

    def test_floats(self):
        """Max is found correctly in a list of floats."""
        self.assertEqual(max_integer([1.5, 2.7, 0.3]), 2.7)


if __name__ == '__main__':
    unittest.main()
