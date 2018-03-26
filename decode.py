def decode(s):
    """Decode a string."""

    # may need to split assertion. valid inputs can have numbers after 0-index.
    # assert s[0].isdigit() and s[1:].isalpha(), "String must contain a sequence that starts with a number and end with letter(s)."

    # will need to store ints as slice starts. grab by index?
    # at end, need to concatenate all valid letters

    # slice_indices = []

    # i = 0

    # for i in range(len(s)):
    #     if s[i].isdigit():
    #         slice_indices.append(i)

    word = ""  # init empty str

    i = 0

    while i < len(s):
        num_to_skip = int(s[i])
        i += num_to_skip + 1

        word += s[i]

        i += 1

    return word

print decode("0t3jsme1hs0t")  # 'test'