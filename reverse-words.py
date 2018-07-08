def reverse_message(message):
    """Takes a list of characters. Words are separated by spaces.
    Returns a message where the words are reversed.

    >>> [ 'c', 'a', 'k', 'e', ' ', 'p', 'o', 'u', 'n', 'd', ' ', 's', 't', 'e', 'a', 'l' ]
    'steal pound cake'
    """

    # we know we've found a whole word when we hit an empty space
    # find indices of spaces
    # slice on spaces(?)
    # travel message backwards - when you hit a space, slice off space index - 1: and append

    reverse_characters(message, 0, len(message) - 1)

    current_word_start_index = 0

    for i in xrange(len(message) + 1):

        if (i == len(message)) or (message[i] == " "):
            reverse_characters(message, current_word_start_index, i - 1)

            current_word_start_index = i + 1

    return message

def reverse_characters(message, left_index, right_index):
    """Helper function that reverses characters."""

    while left_index < right_index:

        message[left_index], message[right_index] = message[right_index], message[left_index]
        left_index += 1
        right_index += 1

    return message