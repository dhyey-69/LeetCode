# 632. Smallest Range Covering Elements from K Lists

# You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.

# We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.

 

# Example 1:

# Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
# Output: [20,24]
# Explanation: 
# List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
# List 2: [0, 9, 12, 20], 20 is in range [20,24].
# List 3: [5, 18, 22, 30], 22 is in range [20,24].
# Example 2:

# Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
# Output: [1,1]
 

# Constraints:

# nums.length == k
# 1 <= k <= 3500
# 1 <= nums[i].length <= 50
# -105 <= nums[i][j] <= 105
# nums[i] is sorted in non-decreasing order.

nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]

def xyz(nums):
        heap = []
        max_value = float('-inf')
        
        for i in range(len(nums)):
            heap.append((nums[i][0], i, 0))
            max_value = max(max_value, nums[i][0])
        
        heap.sort(key=lambda x: x[0])
        
        smallest_range = [-10**5, 10**5]
        
        while True:
            min_value, list_index, element_index = heap[0]
            
            if max_value - min_value < smallest_range[1] - smallest_range[0]:
                smallest_range = [min_value, max_value]
            
            next_index = element_index + 1
            
            if next_index == len(nums[list_index]):
                break
            
            next_value = nums[list_index][next_index]
            heap[0] = (next_value, list_index, next_index)
            
            heap.sort(key=lambda x: x[0])
            
            max_value = max(max_value, next_value)
        
        return smallest_range

print(xyz(nums))