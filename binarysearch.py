def binary_search(val):
    """Using binary search, find val in range 1-100. Return # of guesses."""

    assert 0 < val < 101, "Val must be between 1-100"

    # how many times does 100 need to be halved in a worst-case scenario?
    # current conditionals are oversimplified: need to store if EACH guess is higher or lower than

    guess = 50
    num_guesses = 1  # initialize this first check

    while guess != val:

        if guess > val:  # if val is smaller than 50:
            guess = guess / 2 # try 25
            num_guesses += 1

        else:
            guess = guess + guess / 2  # if val is larger than 50, try 75 (add a quarter)
            num_guesses += 1
    
    return num_guesses
