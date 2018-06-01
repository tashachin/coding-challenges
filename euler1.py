def multiples_three_and_five(max_num):
    """Calculate the sum of all the multiples of 3 and 5 below a given range.

    >>> multiples_three_and_five(10)
    23
    """

    multiples = []

    for num in range(max_num):
        if num % 3 == 0 or num % 5 == 0:
            multiples.append(num)

    return sum(multiples)

print multiples_three_and_five(1000)

if __name__ == "__main__":
    import doctest
    doctest.testmod()