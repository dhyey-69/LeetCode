# 1695. Maximum Erasure Value
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.

# Return the maximum score you can get by erasing exactly one subarray.

# An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).

 

# Example 1:

# Input: nums = [4,2,4,5,6]
# Output: 17
# Explanation: The optimal subarray here is [2,4,5,6].
# Example 2:

# Input: nums = [5,2,1,2,5,2,1,2,5]
# Output: 8
# Explanation: The optimal subarray here is [5,2,1] or [1,2,5].
 

# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104


n = [4,2,4,5,6]

# n = [5,2,1,2,5,2,1,2,5]

def xyz(nums):
    seen = set()
    left = 0
    cur_sum = 0
    best = 0

    for right, x in enumerate(nums):
        while x in seen:
            seen.remove(nums[left])
            cur_sum -= nums[left]
            left += 1

        seen.add(x)
        cur_sum += x

        if cur_sum > best:
            best = cur_sum

    return best

print(xyz(n))