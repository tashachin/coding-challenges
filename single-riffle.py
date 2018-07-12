def is_single_riffle(half1, half2, shuffled_deck):
    """Checks to see if the input deck is a single riffle of two other halves."""

    # right now i don't really understand what the input is
    # output must be a boolean, though

    # smaller function that checks if everything in one half is in the shuffled_deck

    # if shuffled_deck[0] == half1[0] OR shuffled_deck[0] == half2[0], continue
    # else return False

    # is len(shuffled_deck) <= half1 + half2 (?)

    # if first card in deck matches first card in a half, bump up the index for that half

##### ITERATIVE SOLUTION #####

    half1_index = 0
    half2_index = 0
    half1_index_max = len(half1) - 1
    half2_index_max = len(half2) - 1

    for card in shuffled_deck:

        if half1_index <= half1_index_max and card == half1[half1_index]:
            half1_index += 1

        elif half2_index <= half2_index_max and card == half2[half2_index]:
            half2_index += 1

        else:
            return False

    return True

##### RECURSIVE SOLUTION ######

    # if len(shuffled_deck) == 0:
    #     return True

    # if len(half1) and half1[0] == shuffled_deck[0]:
    #     return is_single_riffle(half1[1:], half2, shuffled_deck[1:])

    # elif len(half2) and half2[0] == shuffled_deck[0]:
    #     return is_single_riffle(half1, half2[1:], shuffled_deck[1:])

    # else:
    #     return False