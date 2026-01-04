# 1390. Four Divisors
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors. If there is no such integer in the array, return 0.

 

# Example 1:

# Input: nums = [21,4,7]
# Output: 32
# Explanation: 
# 21 has 4 divisors: 1, 3, 7, 21
# 4 has 3 divisors: 1, 2, 4
# 7 has 2 divisors: 1, 7
# The answer is the sum of divisors of 21 only.
# Example 2:

# Input: nums = [21,21]
# Output: 64
# Example 3:

# Input: nums = [1,2,3,4,5]
# Output: 0
 

# Constraints:

# 1 <= nums.length <= 104
# 1 <= nums[i] <= 105


n = [21,4,7]
# n = [21,21]
# n = [1,2,3,4,5]

def xyz(nums):
    total = 0
        
    for n in nums:
        div_sum = 0
        count = 0
        i = 1
        
        while i * i <= n:
            if n % i == 0:
                j = n // i
                if i == j:
                    count += 1
                    div_sum += i
                else:
                    count += 2
                    div_sum += i + j
            if count > 4:
                break
            i += 1
        
        if count == 4:
            total += div_sum
    
    return total

print(xyz(n))