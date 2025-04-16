# 2537. Count the Number of Good Subarrays
# Medium
# Topics
# Companies
# Hint
# Given an integer array nums and an integer k, return the number of good subarrays of nums.

# A subarray arr is good if there are at least k pairs of indices (i, j) such that i < j and arr[i] == arr[j].

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,1,1,1,1], k = 10
# Output: 1
# Explanation: The only good subarray is the array nums itself.
# Example 2:

# Input: nums = [3,1,4,3,2,2,4], k = 2
# Output: 4
# Explanation: There are 4 different good subarrays:
# - [3,1,4,3,2,2] that has 2 pairs.
# - [3,1,4,3,2,2,4] that has 3 pairs.
# - [1,4,3,2,2,4] that has 2 pairs.
# - [4,3,2,2,4] that has 2 pairs.
 

# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i], k <= 109

n = [1,1,1,1,1]
k = 10

# n = [3,1,4,3,2,2,4]
# k = 2

def xyz(nums,k):
    freq = {}
    left = 0
    pair_count = 0
    result = 0

    for right in range(len(nums)):
        num = nums[right]
        if num in freq:
            pair_count += freq[num]
            freq[num] += 1
        else:
            freq[num] = 1

        while pair_count >= k:
            result += len(nums) - right
            left_num = nums[left]
            freq[left_num] -= 1
            pair_count -= freq[left_num]
            left += 1

    return result

print(xyz(n,k))