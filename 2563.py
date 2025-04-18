# 2563. Count the Number of Fair Pairs
# Medium
# Topics
# Companies
# Hint
# Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.

# A pair (i, j) is fair if:

# 0 <= i < j < n, and
# lower <= nums[i] + nums[j] <= upper
 

# Example 1:

# Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
# Output: 6
# Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).
# Example 2:

# Input: nums = [1,7,9,2,5], lower = 11, upper = 11
# Output: 1
# Explanation: There is a single fair pair: (2,3).
 

# Constraints:

# 1 <= nums.length <= 105
# nums.length == n
# -109 <= nums[i] <= 109
# -109 <= lower <= upper <= 109


n = [0,1,7,4,4,5]
l = 3
u = 6

# n = [1,7,9,2,5]
# l = 11
# u = 11

def xyz(nums,lower,upper):
        nums.sort()
        n = len(nums)
        count = 0

        def lower_bound(arr, target, start):
            lo, hi = start, len(arr)
            while lo < hi:
                mid = (lo + hi) // 2
                if arr[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        def upper_bound(arr, target, start):
            lo, hi = start, len(arr)
            while lo < hi:
                mid = (lo + hi) // 2
                if arr[mid] <= target:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        for i in range(n):
            left = lower - nums[i]
            right = upper - nums[i]
            l = lower_bound(nums, left, i + 1)
            r = upper_bound(nums, right, i + 1)
            count += r - l

        return count

print(xyz(n,l,u))
