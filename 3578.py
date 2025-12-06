# 3578. Count Partitions With Max-Min Difference at Most K
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are given an integer array nums and an integer k. Your task is to partition nums into one or more non-empty contiguous segments such that in each segment, the difference between its maximum and minimum elements is at most k.

# Return the total number of ways to partition nums under this condition.

# Since the answer may be too large, return it modulo 109 + 7.

 

# Example 1:

# Input: nums = [9,4,1,3,7], k = 4

# Output: 6

# Explanation:

# There are 6 valid partitions where the difference between the maximum and minimum elements in each segment is at most k = 4:

# [[9], [4], [1], [3], [7]]
# [[9], [4], [1], [3, 7]]
# [[9], [4], [1, 3], [7]]
# [[9], [4, 1], [3], [7]]
# [[9], [4, 1], [3, 7]]
# [[9], [4, 1, 3], [7]]
# Example 2:

# Input: nums = [3,3,4], k = 0

# Output: 2

# Explanation:

# There are 2 valid partitions that satisfy the given conditions:

# [[3], [3], [4]]
# [[3, 3], [4]]
 

# Constraints:

# 2 <= nums.length <= 5 * 104
# 1 <= nums[i] <= 109
# 0 <= k <= 109.

n = [9,4,1,3,7]
k = 4

# n = [3,3,4]
# k = 0

def xyz(nums,k):
    MOD = 10**9 + 7
    n = len(nums)

    dp = [0] * (n + 1)
    pref = [0] * (n + 1)
    dp[0] = 1
    pref[0] = 1

    maxd = []
    mind = []

    j = 0
    for i in range(n):

        while maxd and maxd[-1] < nums[i]:
            maxd.pop()
        maxd.append(nums[i])

        while mind and mind[-1] > nums[i]:
            mind.pop()
        mind.append(nums[i])

        while maxd[0] - mind[0] > k:
            if maxd[0] == nums[j]:
                maxd.pop(0)
            if mind[0] == nums[j]:
                mind.pop(0)
            j += 1

        if j > 0:
            dp[i+1] = (pref[i] - pref[j-1]) % MOD
        else:
            dp[i+1] = pref[i] % MOD

        pref[i+1] = (pref[i] + dp[i+1]) % MOD

    return dp[n] % MOD

print(xyz(n,k))