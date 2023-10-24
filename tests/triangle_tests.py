import unittest

from methods.triangle import *


class TriangleTestCase(unittest.TestCase):
    def test_zero_area_1(self):
        result = area(15, 0)
        expected_result = 0
        self.assertEqual(expected_result, result)

    def test_zero_area_2(self):
        result = area(0, 15)
        expected_result = 0
        self.assertEqual(expected_result, result)

    def test_small_data_area(self):
        result = area(30, 239)
        expected_result = 3585
        self.assertEqual(expected_result, result)

    def test_large_data_area(self):
        result = area(11111111111, 9876543210)
        expected_result = 5.48696844994513031e+19
        self.assertEqual(expected_result, result)

    def test_large_data_perimeter(self):
        result = perimeter(1234567890, 9876543210, 5826873526534872)
        expected_result = 5826884637645972
        self.assertEqual(expected_result, result)

    def test_small_data_perimeter(self):
        result = perimeter(5, 432, 47)
        expected_result = 484
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
