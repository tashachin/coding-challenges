def reverse(characters):
    """Reverses a list of characters in place.

    >>> "hello"
    "olleh"

    >>> "How are you?"
    "?uoy era woH"
    """

    left_index = 0
    right_index = len(characters) - 1

    while left_index < right_index:

        characters[left_index], characters[right_index] = characters[right_index], characters[left_index]

        left_index += 1
        right_index -= 1

    return characters
