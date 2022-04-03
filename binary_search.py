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
