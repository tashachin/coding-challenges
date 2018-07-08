def first_duplicate(a):
    """If an array contains duplicates, returns the first duplicate with the smallest index.

    If there are no duplicates, return -1

    >>> [2, 1, 3, 5, 3, 2]
    3

    >>> [2, 4, 3, 5, 1]
    -1
    """

    # need to check every element in list
    # is best runtime O(n)?
    # need to store indices of nums as well
    
    seen_nums = []
    duplicate_nums_and_indices = []
    
    # check if number already been seen, then store index
    
    for i in xrange(len(a)):
        
        if a[i] in seen_nums:
            duplicate_nums_and_indices.append((a[i], i))
        
        seen_nums.append(a[i])
    
    if not duplicate_nums_and_indices:
        return -1
    
    min_num = duplicate_nums_and_indices[0][0]
    min_index = duplicate_nums_and_indices[0][1]
    
    for num, index in duplicate_nums_and_indices[1:]:
        
        if index < min_index:
            min_index = index
            min_num = num
        
    return min_num

# Current solution does not pass runtime for all test cases on codefights.