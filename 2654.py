# 2654. Minimum Number of Operations to Make All Array Elements Equal to 1
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are given a 0-indexed array nums consisiting of positive integers. You can do the following operation on the array any number of times:

# Select an index i such that 0 <= i < n - 1 and replace either of nums[i] or nums[i+1] with their gcd value.
# Return the minimum number of operations to make all elements of nums equal to 1. If it is impossible, return -1.

# The gcd of two integers is the greatest common divisor of the two integers.

 

# Example 1:

# Input: nums = [2,6,3,4]
# Output: 4
# Explanation: We can do the following operations:
# - Choose index i = 2 and replace nums[2] with gcd(3,4) = 1. Now we have nums = [2,6,1,4].
# - Choose index i = 1 and replace nums[1] with gcd(6,1) = 1. Now we have nums = [2,1,1,4].
# - Choose index i = 0 and replace nums[0] with gcd(2,1) = 1. Now we have nums = [1,1,1,4].
# - Choose index i = 2 and replace nums[3] with gcd(1,4) = 1. Now we have nums = [1,1,1,1].
# Example 2:

# Input: nums = [2,10,6,14]
# Output: -1
# Explanation: It can be shown that it is impossible to make all the elements equal to 1.
 

# Constraints:

# 2 <= nums.length <= 50
# 1 <= nums[i] <= 106


n = [2,6,3,4]
# n = [2,10,6,14]

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def xyz(nums):
    n = len(nums)
    
    g = 0
    for num in nums:
        g = gcd(g, num)
    if g > 1:
        return -1

    ones = 0
    for num in nums:
        if num == 1:
            ones += 1
    if ones > 0:
        return n - ones

    min_len = n + 1
    for i in range(n):
        g = nums[i]
        for j in range(i + 1, n):
            g = gcd(g, nums[j])
            if g == 1:
                length = j - i + 1
                if length < min_len:
                    min_len = length
                break

    if min_len == n + 1:
        return -1
    return (min_len - 1) + (n - 1)

print(xyz(n))