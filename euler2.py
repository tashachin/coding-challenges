def sum_even_fibonacci(max_term):
    """Returns the sum of all the even Fibonacci terms within the specified range.

    >>> sum_even_fibonacci(89)
    44
    """

    fibs = fibonacci(max_term)

    even_fibs = []

    for fib in fibs:
        if fib % 2 == 0:
            even_fibs.append(fib)

    return sum(even_fibs)

def fibonacci(max_term):
    """Calculate fibonacci WITHOUT recursion."""

    fibs = [0, 1]

    while True:
        new_fib = fibs[-1] + fibs[-2]

        if new_fib > max_term:
            break

        fibs.append(new_fib)

    return fibs

print sum_even_fibonacci(4000000)

if __name__ == "__main__":
    import doctest
    doctest.testmod()