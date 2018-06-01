def reduce_string(string):
    """Whenever an 'e' shows up consecutively in a string, reduce it to just once instance of the letter.

    >>> reduce_string('askfheeeelkjeeeemahee')
    'askfhelkjemahe'
    """

    # when checking e, need to also peek at next item
    # if that item is also an e, we need to get rid of it
    # problem becomes trying to index out
    # do i need to solve this recursively?

    valid_string = []

    for i in range(len(string)):
        if string[i] != "e":
            valid_string.append(string[i])

        else:
            # in the case that the letter IS an e, we check that the letter before is not an e before appending
            if string[i-1] != "e":
                valid_string.append(string[i])

    return "".join(valid_string)

if __name__ == "__main__":
    import doctest
    doctest.testmod()