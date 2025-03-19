# 3191. Minimum Operations to Make Binary Array Elements Equal to One I
# Medium
# Topics
# Companies
# Hint
# You are given a binary array nums.

# You can do the following operation on the array any number of times (possibly zero):

# Choose any 3 consecutive elements from the array and flip all of them.
# Flipping an element means changing its value from 0 to 1, and from 1 to 0.

# Return the minimum number of operations required to make all elements in nums equal to 1. If it is impossible, return -1.

 

# Example 1:

# Input: nums = [0,1,1,1,0,0]

# Output: 3

# Explanation:
# We can do the following operations:

# Choose the elements at indices 0, 1 and 2. The resulting array is nums = [1,0,0,1,0,0].
# Choose the elements at indices 1, 2 and 3. The resulting array is nums = [1,1,1,0,0,0].
# Choose the elements at indices 3, 4 and 5. The resulting array is nums = [1,1,1,1,1,1].
# Example 2:

# Input: nums = [0,1,1,1]

# Output: -1

# Explanation:
# It is impossible to make all elements equal to 1.

 

# Constraints:

# 3 <= nums.length <= 105
# 0 <= nums[i] <= 1

# n = [0,1,1,1,0,0]
n = [0,1,1,1]

def xyz(nums):
    n = len(nums)
    count = 0
    res = [1] * n

    for i in range(n - 2):
        if nums[i] == 0:  
            nums[i] = 1 - nums[i]
            nums[i + 1] = 1 - nums[i + 1]
            nums[i + 2] = 1 - nums[i + 2]
            count += 1

    return count if nums == res else -1
        
print(xyz(n))