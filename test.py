import unittest

from formater import formatted_name
from fibonachi import Fibonacci
from unittest import TestCase


class TestFibonacci(TestCase):
    def setUp(self):
        self.fibonacci_test_suite = [
            [1, 1], [2, 1], [3, 2], [4, 3],
            [5, 5], [6, 8], [7, 13], [8, 21],
            [9, 34], [10, 55], [11, 89], [12, 144]
        ]

    def test_fibonacci_data_suite(self):
        fib = Fibonacci()
        for n, expected_number in self.fibonacci_test_suite:
            actual_number = fib(n)
            self.assertEqual(expected_number, actual_number)

    def test_fibonacci_1_2_5(self):
        fib = Fibonacci()
        x = fib(1)
        self.assertEqual(1, x, f"Filed 1-st the fibonacci = {x} - FAILED")
        x = fib(2)
        self.assertEqual(1, x, f"Filed 2-nd the fibonacci = {x} - FAILED")
        x = fib(5)
        self.assertEqual(5, x, f"Filed 5-th the fibonacci = {x} - FAILED")

    def test_fibonachi_negative_figure(self):
        fib = Fibonacci()
        self.assertRaises(ValueError, fib, -1)


class TestFormatter(TestCase):
    def setUp(self):
        self.first_name = "First"
        self.last_name = "Last"
        self.middle_name = "Middle"
        self.first_last = self.first_name + " " + self.last_name
        self.first_midle_last = self.first_name + " " + self.middle_name + " " + self.last_name

    def test_first_last(self):
        self.assertEqual(formatted_name(self.first_name, self.last_name) , self.first_last)

    def test_first_midle_last(self):
        self.assertEqual(formatted_name(self.first_name, self.last_name, self.middle_name), self.first_midle_last)

    def test_exception_middle(self):
        self.assertRaises(TypeError, formatted_name, self.first_name, self.last_name, -1)


unittest.main(argv=[''], verbosity=2, exit=False)


