from module_factorial.factorial import *


def test_factorial_iterative_6():
    """Test factorial_iterative function with input 6."""
    actual = factorial_iterative(6)
    expected = 720
    assert actual == expected


def test_factorial_iterative_5():
    """Test factorial_iterative function with input 5."""
    actual = factorial_iterative(5)
    expected = 120
    assert actual == expected


def test_factorial_iterative_4():
    """Test factorial_iterative function with input 4."""
    actual = factorial_iterative(4)
    expected = 24
    assert actual == expected


# ------------------------------------------------------------------


def test_factorial_recursion_6():
    """Test factorial_recursion function with input 6."""
    actual = factorial_recursion(6)
    expected = 720
    assert actual == expected


def test_factorial_recursion_5():
    """Test factorial_recursion function with input 5."""
    actual = factorial_recursion(5)
    expected = 120
    assert actual == expected


def test_factorial_recursion_4():
    """Test factorial_recursion function with input 4."""
    actual = factorial_recursion(4)
    expected = 24
    assert actual == expected


# --------------------------------------------------------------------


def test_clumsy_factorial_0():
    """Test clumsy_factorial function with input 0."""
    actual = clumsy_factorial(0)
    expected = 1
    assert actual == expected


def test_clumsy_factorial_1():
    """Test clumsy_factorial function with input 1."""
    actual = clumsy_factorial(1)
    expected = 1
    assert actual == expected


def test_clumsy_factorial_5():
    """Test clumsy_factorial function with input 5."""
    actual = clumsy_factorial(5)
    expected = 4
    assert actual == expected


def test_clumsy_factorial_6():
    """Test clumsy_factorial function with input 6."""
    actual = clumsy_factorial(6)
    expected = 8
    assert actual == expected


def test_clumsy_factorial_8():
    """Test clumsy_factorial function with input 8."""
    actual = clumsy_factorial(8)
    expected = 9
    assert actual == expected
