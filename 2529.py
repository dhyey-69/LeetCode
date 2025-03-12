# 2529. Maximum Count of Positive Integer and Negative Integer
# Easy
# Topics
# Companies
# Hint
# Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers.

# In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, then return the maximum of pos and neg.
# Note that 0 is neither positive nor negative.

 

# Example 1:

# Input: nums = [-2,-1,-1,1,2,3]
# Output: 3
# Explanation: There are 3 positive integers and 3 negative integers. The maximum count among them is 3.
# Example 2:

# Input: nums = [-3,-2,-1,0,0,1,2]
# Output: 3
# Explanation: There are 2 positive integers and 3 negative integers. The maximum count among them is 3.
# Example 3:

# Input: nums = [5,20,66,1314]
# Output: 4
# Explanation: There are 4 positive integers and 0 negative integers. The maximum count among them is 4.
 

# Constraints:

# 1 <= nums.length <= 2000
# -2000 <= nums[i] <= 2000
# nums is sorted in a non-decreasing order.

# n = [-2,-1,-1,1,2,3]
# n = [-3,-2,-1,0,0,1,2]
# n = [5,20,66,1314]
n = [-1924,-1910,-1840,-1797,-1714,-1640,-1638,-1567,-1564,-1409,-1141,-1115,-1068,-658,-465,-447,-434,-386,-321,-191,-186,-127,-63,69,186,253,334,401,482,805,809,812,833,913,955,991,1113,1128,1133,1178,1204,1570,1616,1725,1729,1787,1853,1943,1980,1980]

def xyz(nums):
    neg , pos , zero_count = 0 , 0 , 0

    for i in range(len(nums)):
        if nums[i] < 0:
            neg += 1
        elif nums[i] > 0:
            pos = len(nums) - neg - zero_count
            break
        else:
            zero_count += 1
    
    return max( pos , neg )

print(xyz(n))