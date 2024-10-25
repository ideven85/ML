import unittest

from src.fib import memoized_fib, fib


def test_fib():
    assert memoized_fib(10) == 55
    assert list(fib(10)) == list(fib(10)) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
