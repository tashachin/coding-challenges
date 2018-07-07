def binary_search(target, nums):
    """A basic implementation of a binary search.

    Input: int, list of ints
    Output: boolean
    """

    # establish the range of nums to check
    floor_index = -1
    ceiling_index = len(nums)

    # we leave a gap between the floor index and ceiling index,
    # because a lack of space means the target is not in nums
    while floor_index + 1 < ceiling_index:

        distance = ceiling_index - floor_index
        half_distance = distance / 2
        guess_index = floor_index + half_distance

        guess_value = nums[guess_index]

        if guess_value == target:
            return True

        if guess_value > target:
            ceiling_index = guess_index

        else:
            floor_index = guess_index

    return False
