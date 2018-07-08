def merge_sorted_lists(lst1, lst2):
    """Takes two sorted arrays and returns a single sorted array."""

    merged_list_size = len(lst1) + len(lst2)
    merged_list = [None] * merged_list_size

    current_index_lst1 = 0
    current_index_lst2 = 0
    current_index_merged = 0

    while current_index_merged < merged_list_size:

        if current_index_lst1 >= len(current_index_lst1):
            
            first_unmerged_lst1 = lst1[current_index_lst1]
            first_unmerged_lst2 = lst2[current_index_lst2]

        if first_unmerged_lst1 < first_unmerged_lst2:
            merged_list[current_index_merged] = first_unmerged_lst1
            current_index_lst1 += 1

        else:
            merged_list[current_index_merged] = first_unmerged_lst2
            current_index_lst2 += 1

        current_index_merged += 1

    return merged_list