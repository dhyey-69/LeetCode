# 962. Maximum Width Ramp

# A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i] <= nums[j]. The width of such a ramp is j - i.

# Given an integer array nums, return the maximum width of a ramp in nums. If there is no ramp in nums, return 0.

 

# Example 1:

# Input: nums = [6,0,8,2,1,5]
# Output: 4
# Explanation: The maximum width ramp is achieved at (i, j) = (1, 5): nums[1] = 0 and nums[5] = 5.
# Example 2:

# Input: nums = [9,8,1,0,1,9,4,0,4,1]
# Output: 7
# Explanation: The maximum width ramp is achieved at (i, j) = (2, 9): nums[2] = 1 and nums[9] = 1.
 

# Constraints:

# 2 <= nums.length <= 5 * 104
# 0 <= nums[i] <= 5 * 104

# n = [6,0,8,2,1,5]
n = [9,8,1,0,1,9,4,0,4,1]

def xyz(nums):
    # a = 0
    
    # for i in range(1,len(nums)):
    #     print("A =",nums[a])
    #     print("I =",nums[i])
    #     if nums[a] > nums[i]:
    #         nums[a] = nums[i]
    #         a += 1
        
    # return i-a

    sorted_nums_index = sorted(range(len(nums)), key=lambda i: nums[i])
    max_w = 0
    min_index = float('inf')

    for i in sorted_nums_index:
        min_index = min(min_index , i)
        max_w = max(max_w , i - min_index)

    return max_w
        

print(xyz(n))