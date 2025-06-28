# 2099. Find Subsequence of Length K With the Largest Sum
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k that has the largest sum.

# Return any such subsequence as an integer array of length k.

# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

# Example 1:

# Input: nums = [2,1,3,3], k = 2
# Output: [3,3]
# Explanation:
# The subsequence has the largest sum of 3 + 3 = 6.
# Example 2:

# Input: nums = [-1,-2,3,4], k = 3
# Output: [-1,3,4]
# Explanation: 
# The subsequence has the largest sum of -1 + 3 + 4 = 6.
# Example 3:

# Input: nums = [3,4,3,3], k = 2
# Output: [3,4]
# Explanation:
# The subsequence has the largest sum of 3 + 4 = 7. 
# Another possible subsequence is [4, 3].
 

# Constraints:

# 1 <= nums.length <= 1000
# -105 <= nums[i] <= 105
# 1 <= k <= nums.length


n = [2,1,3,3]
k = 2

# n = [-1,-2,3,4]
# k = 3

# n = [3,4,3,3]
# k = 2

def xyz(nums,k):
    indexed = list(enumerate(nums))
        
    top_k = sorted(indexed, key=lambda x: x[1], reverse=True)[:k]
    
    top_k_sorted = sorted(top_k, key=lambda x: x[0])
    
    return [val for idx, val in top_k_sorted]

print(xyz(n,k))