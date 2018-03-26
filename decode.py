def decode(s):
    """Decode a string."""

    # may need to split assertion. valid inputs can have numbers after 0-index.
    # assert s[0].isdigit() and s[1:].isalpha(), "String must contain a sequence that starts with a number and end with letter(s)."

    # will need to store ints as slice starts. grab by index?
    # at end, need to concatenate all valid letters

    slice_indices = []

    i = 0

    for i in range(len(s)):
        if s[i].isdigit():
            slice_indices.append(i)

    