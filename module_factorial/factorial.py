def factorial_iterative(n):
    """Calculate the factorial of a non-negative integer n iteratively."""
    if n <= 1:
        return 1
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result


def factorial_recursion(n):
    """Calculate the factorial of a non-negative integer n recursively."""
    if n <= 1:
        return 1
    return n * factorial_recursion(n - 1)


def clumsy_factorial(n):
    """
    Calculate the 'clumsy factorial' of a positive integer n.

    The 'clumsy factorial' is defined as a fixed rotation of arithmetic
    operations on consecutive integers in decreasing order.

    Args:
        n (int): A positive integer.

    Returns:
        int: The 'clumsy factorial' of n.

    Notes:
        - For n = 0 or n = 1, the clumsy factorial is 1.
        - For n = 2, the clumsy factorial is 2.
        - For n = 3, the clumsy factorial is 6.
        - For n = 4, the clumsy factorial is 7.
        - For n > 4, the clumsy factorial follows a fixed pattern based on the remainder of n modulo 4.
    """
    # Base cases
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 6
    elif n == 4:
        return 7

    # Recursive case
    if n % 4 == 0:
        return n + 1
    elif n % 4 == 3:
        return n - 1
    elif n % 4 == 2:
        return n + 2
    else:  # n % 4 == 1
        return n - 2 + clumsy_factorial(n - 4)


# I tried