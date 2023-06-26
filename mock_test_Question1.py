
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:
# Input: nums = [0]
# Output: [0]

# Constraints:
# a. 1 <= nums.length <= 10^4
# b. -2^31 <= nums[i] <= 2^31 - 1


def moveZeroes(nums):
    """
    Moves all zeros to the end of the array while maintaining the relative order of non-zero elements.
    """
    n = len(nums)
    left = 0  # Pointer to track non-zero elements

    # Traverse the array
    for i in range(n):
        if nums[i] != 0:
            # Move non-zero element to the left pointer position
            nums[left] = nums[i]
            left += 1

    # Fill the remaining elements with zeros
    for i in range(left, n):
        nums[i] = 0

# Example usage
nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)
