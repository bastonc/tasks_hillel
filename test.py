import unittest

import pytest

from formater import formatted_name
from fibonachi import Fibonacci
from unittest import TestCase


class TestFibonacci(TestCase):
    def setUp(self):
        self.fib = Fibonacci()

    def test_fibonacci_1(self):
        x = self.fib(1)
        self.assertEqual(1, x, f"Filed 1-st the fibonacci = {x} - FAILED")

    def test_fibonacci_2(self):
        x = self.fib(2)
        self.assertEqual(1, x, f"Filed 2-nd the fibonacci = {x} - FAILED")

    def test_fibonacci_5(self):
        x = self.fib(5)
        self.assertEqual(5, x, f"Filed 5-th the fibonacci = {x} - FAILED")

    def test_fibonacci_negative_figure(self):
        self.assertRaises(ValueError, self.fib, -1)

    def test_fibonacci_zero(self):
        x = self.fib(0)
        self.assertEqual(0, x, f"Filed 0-th the fibonacci = {x} - FAILED")

    def test_fibonacci_big_figure(self):
        x = self.fib(100)
        self.assertEqual(354224848179261915075, x, f"Filed 100-th the fibonacci = {x} - FAILED")

    def test_fibonacci_over_big_figure(self):
        self.assertRaises(RecursionError, self.fib, 1000)


@pytest.mark.timeout(1)
def test_fibonacci_long_time_runing():
    Fibonacci().__call__(450)


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


