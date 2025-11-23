# 1262. Greatest Sum Divisible by Three
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer array nums, return the maximum possible sum of elements of the array such that it is divisible by three.

 

# Example 1:

# Input: nums = [3,6,5,1,8]
# Output: 18
# Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).
# Example 2:

# Input: nums = [4]
# Output: 0
# Explanation: Since 4 is not divisible by 3, do not pick any number.
# Example 3:

# Input: nums = [1,2,3,4,4]
# Output: 12
# Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).
 

# Constraints:

# 1 <= nums.length <= 4 * 104
# 1 <= nums[i] <= 104


n = [3,6,5,1,8]
# n = [4]
# n = [1,2,3,4,4]

def xyz(nums):
    total = sum(nums)

    r1 = []
    r2 = []
    for x in nums:
        if x % 3 == 1:
            r1.append(x)
        elif x % 3 == 2:
            r2.append(x)

    r1.sort()
    r2.sort()

    mod = total % 3
    if mod == 0:
        return total

    remove = float('inf')
    if mod == 1:
        if r1:
            remove = min(remove, r1[0])
        if len(r2) >= 2:
            remove = min(remove, r2[0] + r2[1])

    else:
        if r2:
            remove = min(remove, r2[0])
        if len(r1) >= 2:
            remove = min(remove, r1[0] + r1[1])

    return total - remove if remove != float('inf') else 0

print(xyz(n))