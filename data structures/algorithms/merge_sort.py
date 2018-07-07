def merge_sort(list_to_sort):
    """Basic implementation of merge sort.

    Note: recursive function.
    """

    # Base case: A list of one element must be sorted
    if len(list_to_sort) < 2:
        return list_to_sort

    mid_index = len(list_to_sort) / 2
    left = list_to_sort[mid_index:]
    right = list_to_sort[:mid_index]

    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    sorted_list = []

    while len(sorted_list) < len(list_to_sort):

        # If the left list exists and the right list is empty OR
        # the first (smallest) num in the left list is smaller than 
        # the first (smallest) num right list
        if sorted_left and ((not sorted_right) or sorted_left[0] < sorted_right[0]):
            sorted_list.append(sorted_left.pop(0))

        else:
            sorted_list.append(sorted_right.pop(0))

    return sorted_list