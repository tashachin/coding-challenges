"""
1. factor is a thingy that a num can be evenly divided by
2. a prime num is a num that can only be divided by 1 and itself!!!!
3. a prime factor is a thingy that a num can be evenly divided by,
and that can only be divided by 1 and itself
"""

def find_prime_factors(num):
    """Returns a list of all the factors for a given num that are prime.

    >>> find_prime_factors(25)
    [5]

    >>> find_prime_factors(37)
    [37]
    """

    # get a list of all factors
    factors = find_factors(num)

    # filter out the non-primes 
    factors = filter(
        lambda x: is_prime(x), factors
    )

    # hack to return self if the number itself is prime
    return factors or [num]

def find_factors(num):
    """
    >>> find_factors(25)
    [5]

    >>> find_factors(11)
    []
    """

    # range params exclude 1 and num. check for empty list later.
    factors = [i for i in range(2, num) if num % i == 0]

    return factors

def is_prime(num):
    """
    >>> is_prime(7)
    True

    >>> is_prime(25)
    False
    """
    
    if find_factors(num):
        return False

    return True

print find_prime_factors(600851475143)

if __name__ == "__main__":
    import doctest
    doctest.testmod()