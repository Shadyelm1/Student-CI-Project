import unittest

from app.calculator import (
    add_numbers,
    subtract_numbers,
    multiply_numbers,
    divide_numbers,
)


class TestCalculator(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add_numbers(-2, -3), -5)

    def test_subtract_numbers(self):
        self.assertEqual(subtract_numbers(7, 4), 3)

    def test_multiply_numbers(self):
        self.assertEqual(multiply_numbers(6, 5), 30)

    def test_divide_numbers(self):
        self.assertEqual(divide_numbers(8, 2), 4)

    def test_divide_by_zero_raises(self):
        with self.assertRaises(ValueError):
            divide_numbers(1, 0)


if __name__ == "__main__":
    unittest.main()
