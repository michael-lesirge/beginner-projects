def binary_search(nums, target: int) -> int:
    """
    returns the index of the target in nums if it exists else it returns -1
    only works for sorted lists
    takes O(log n) time and O(1) space
    """
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        mid_num = nums[mid]
        if mid_num == target:
            return mid
        elif mid_num > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

def peak_finder(nums):
    """
    returns the index of a peak in a list if it exists else it returns -1
    takes O(log n) time and O(1) space
    """
    # set left and right side
    left = 0
    right = len(nums)

    # add negative infinity to each side to not go out of bounds with nums[mid + or - 1]
    nums = [float('-inf')] + nums + [float('-inf')]

    while left <= right:
        # locate mid
        mid = (left + right) // 2
        mid_num = nums[mid]

        # classic divide and conquer approach
        if mid_num < nums[mid + 1]:
            left = mid + 1
        elif mid_num < nums[mid - 1]:
            right = mid - 1

        # if this is reached than a peak has been found
        else:
            return mid - 1  # subtract one to compensate for adding -inf to beginning

    # fall back
    return -1
