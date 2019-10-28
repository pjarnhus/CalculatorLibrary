"""
Unit tests for the calculator library.
"""

import calculator


def test_addition():
    assert calculator.add(2, 2) == 4


def test_subtraction():
    assert calculator.subtract(4, 2) == 2
