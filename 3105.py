# 3105. Longest Strictly Increasing or Strictly Decreasing Subarray
# Easy
# Topics
# Companies
# You are given an array of integers nums. Return the length of the longest 
# subarray
#  of nums which is either 
# strictly increasing
#  or 
# strictly decreasing
# .

 

# Example 1:

# Input: nums = [1,4,3,3,2]

# Output: 2

# Explanation:

# The strictly increasing subarrays of nums are [1], [2], [3], [3], [4], and [1,4].

# The strictly decreasing subarrays of nums are [1], [2], [3], [3], [4], [3,2], and [4,3].

# Hence, we return 2.

# Example 2:

# Input: nums = [3,3,3,3]

# Output: 1

# Explanation:

# The strictly increasing subarrays of nums are [3], [3], [3], and [3].

# The strictly decreasing subarrays of nums are [3], [3], [3], and [3].

# Hence, we return 1.

# Example 3:

# Input: nums = [3,2,1]

# Output: 3

# Explanation:

# The strictly increasing subarrays of nums are [3], [2], and [1].

# The strictly decreasing subarrays of nums are [3], [2], [1], [3,2], [2,1], and [3,2,1].

# Hence, we return 3.

 

# Constraints:

# 1 <= nums.length <= 50
# 1 <= nums[i] <= 50

# n = [1,4,3,3,2]
# n = [3,3,3,3]
n = [3,2,1]

def xyz(nums):
    if not nums:
        return 0
    
    in_count = 1
    dec_count = 1
    max_length = 1

    for i in range(1,len(nums)):
        if nums[i] < nums[i-1]:
            dec_count += 1
            in_count = 1
        elif nums[i] > nums[i-1]:
            in_count += 1
            dec_count = 1
        else:
            in_count = 1
            dec_count = 1
    
        max_length = max(max_length,in_count,dec_count)
    
    return max_length

print(xyz(n))