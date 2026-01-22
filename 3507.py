# 3507. Minimum Pair Removal to Sort Array I
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an array nums, you can perform the following operation any number of times:

# Select the adjacent pair with the minimum sum in nums. If multiple such pairs exist, choose the leftmost one.
# Replace the pair with their sum.
# Return the minimum number of operations needed to make the array non-decreasing.

# An array is said to be non-decreasing if each element is greater than or equal to its previous element (if it exists).

 

# Example 1:

# Input: nums = [5,2,3,1]

# Output: 2

# Explanation:

# The pair (3,1) has the minimum sum of 4. After replacement, nums = [5,2,4].
# The pair (2,4) has the minimum sum of 6. After replacement, nums = [5,6].
# The array nums became non-decreasing in two operations.

# Example 2:

# Input: nums = [1,2,2]

# Output: 0

# Explanation:

# The array nums is already sorted.

 

# Constraints:

# 1 <= nums.length <= 50
# -1000 <= nums[i] <= 1000



n = [5,2,3,1]
# n = [1,2,2]

def xyz(nums):
    def is_sorted(arr):
        return all(arr[i] >= arr[i - 1] for i in range(1, len(arr)))

    ops = 0

    while not is_sorted(nums):
        min_sum = float('inf')
        idx = 0

        for i in range(len(nums) - 1):
            s = nums[i] + nums[i + 1]
            if s < min_sum:
                min_sum = s
                idx = i

        nums = nums[:idx] + [nums[idx] + nums[idx + 1]] + nums[idx + 2:]
        ops += 1

    return ops

print(xyz(n))