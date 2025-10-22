# 3347. Maximum Frequency of an Element After Performing Operations II
# Hard
# Topics
# premium lock icon
# Companies
# Hint
# You are given an integer array nums and two integers k and numOperations.

# You must perform an operation numOperations times on nums, where in each operation you:

# Select an index i that was not selected in any previous operations.
# Add an integer in the range [-k, k] to nums[i].
# Return the maximum possible frequency of any element in nums after performing the operations.

 

# Example 1:

# Input: nums = [1,4,5], k = 1, numOperations = 2

# Output: 2

# Explanation:

# We can achieve a maximum frequency of two by:

# Adding 0 to nums[1], after which nums becomes [1, 4, 5].
# Adding -1 to nums[2], after which nums becomes [1, 4, 4].
# Example 2:

# Input: nums = [5,11,20,20], k = 5, numOperations = 1

# Output: 2

# Explanation:

# We can achieve a maximum frequency of two by:

# Adding 0 to nums[1].
 

# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# 0 <= k <= 109
# 0 <= numOperations <= nums.length


n = [1,4,5]
k = 1
nOp = 2

# n = [5,11,20,20]
# k = 5
# nOp = 1

def _find_bisect_left(arr, x):
    low = 0
    high = len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        else:
            high = mid
    return low

def _find_bisect_right(arr, x):
    low = 0
    high = len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] <= x:
            low = mid + 1
        else:
            high = mid
    return low

def xyz(nums,k,numOperations):

    n = len(nums)
    nums.sort()
    
    potential_targets = set()
    for x in nums:
        potential_targets.add(x)
        potential_targets.add(x - k)
        potential_targets.add(x + k)
        
    max_freq = 0
    
    for target in potential_targets:
        low_val = target - k
        high_val = target + k
        
        idx_low = _find_bisect_left(nums, low_val)
        idx_high = _find_bisect_right(nums, high_val)
        
        total_in_range = idx_high - idx_low
        
        if total_in_range == 0:
            continue
            
        idx_target_low = _find_bisect_left(nums, target)
        idx_target_high = _find_bisect_right(nums, target)
        
        base_score = idx_target_high - idx_target_low
        
        potential_converts = total_in_range - base_score
        
        current_freq = base_score + min(potential_converts, numOperations)
        
        max_freq = max(max_freq, current_freq)
        
    return max_freq

print(xyz(n,k,nOp))