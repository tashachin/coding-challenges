"""
1. factor is a thingy that a num can be evenly divided by
2. a prime num is a num that can only be divided by 1 and itself!!!!
3. a prime factor is a thingy that a num can be evenly divided by,
and that can only be divided by 1 and itself
"""

import math

def find_prime_factors(num):
    """Returns a list of all the factors for a given num that are prime.

    >>> find_prime_factors(25)
    5

    >>> find_prime_factors(20)
    5

    >>> find_prime_factors(37)
    37
    """

    # range params exclude 1 and num. check for empty list later.
    # factors = [i for i in range(2, num) if num % i == 0]
    factors = []

    if num % 2 == 0:
        factors.append(2)
        num = num / 2
        # print factors, "after 2 logic"

def alter_range():
    pass
    # i all odd nums after 1, typecast to avoid floats
    # range is stop exclusive
    # step by 2 to avoid evens
    for i in range(3, num + 1, 2):
        # print i, "in for loop"
        while num % i == 0:
            factors.append(i)
            num = num / i

    # print factors

    return max(factors)

# print find_prime_factors(600851475143)

# def is_prime(num):
#     """
#     >>> is_prime(7)
#     True

#     >>> is_prime(25)
#     False
#     """
    
#     if find_factors(num):
#         return False

#     return True

# print find_prime_factors(600851475143)

if __name__ == "__main__":
    import doctest
    doctest.testmod()