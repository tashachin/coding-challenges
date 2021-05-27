"""Interview Cake: Merge Sort
In order to win the prize for most cookies sold, my friend Alice and I are going to merge our Girl Scout Cookies orders and enter as one unit.

Each order is represented by an "order id" (an integer).

We have our lists of orders sorted numerically already, in lists. Write a function to merge our lists of orders into one sorted list.
"""
# I like to start by defining a function stub.
def sorted_cookie_orders(ord1, ord2):
    """Takes two sorted lists and returns a merged sorted list.

    >>> [1, 3, 5, 8], [2, 4, 6, 7, 10]
    [1, 2, 3, 4, 5, 6, 7, 8, 10]""" # This docstring will run in Python's interpretive mode.

    # len(lst) returns the num of elements in the list.
    cookie_orders_size = len(ord1) + len(ord2) # 4 + 5 = 9

    # None is a reserved keyword that takes up a single element in an otherwise empty list.
    # [] is not equivalent to [None]
    cookie_orders = [None] * cookie_orders_size # 1 * 9 = 9

    start_of_ord1 = ord1[0] # 1
    start_of_ord2 = ord2[0] # 2

    if start_of_ord1 < start_of_ord2:
        cookie_orders[0] = start_of_ord1 # 1

    else:
        cookie_orders[0] = start_of_ord2 # Does not execute in our test case.

if __name__ == "__main__":
    import doctest
    doctest.testmod()
