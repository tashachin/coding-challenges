def count_recursively(lst):
    """Return number of items in a list, using recursion.

    >>> count_recursively([])
	0

	>>> count_recursively([1, 2, 3])
	3"""

    if not lst:  # my base case assumption was correct
        return 0

    return 1 + count_recursively(lst[1:])  # originally i meant to pop off elements but slicing ensures a new copy of a shrinking list