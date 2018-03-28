def spoonerize(words):
    # i'm turning the input into a list of strs
    # i want to swap the strs at 0 with one another but strs are immutable
    spooned_words = []
    words = words.split()

    first_word = words[0]
    second_word = words[1]

    spooned_words.append(first_word[0] + second_word[1:])
    spooned_words.append(second_word[0] + first_word[1:])
    
    return (" ").join(spooned_words)

print spoonerize("spoonerize me")  # mpoonerize se

# time complexity: O(n) because of .split() and .join()
# bit more space complexity because slicing creates new strings