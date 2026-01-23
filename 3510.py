# 3510. Minimum Pair Removal to Sort Array II
# Hard
# Topics
# premium lock icon
# Companies
# Hint
# Given an array nums, you can perform the following operation any number of times:

# Select the adjacent pair with the minimum sum in nums. If multiple such pairs exist, choose the leftmost one.
# Replace the pair with their sum.
# Return the minimum number of operations needed to make the array non-decreasing.

# An array is said to be non-decreasing if each element is greater than or equal to its previous element (if it exists).

 

# Example 1:

# Input: nums = [5,2,3,1]

# Output: 2

# Explanation:

# The pair (3,1) has the minimum sum of 4. After replacement, nums = [5,2,4].
# The pair (2,4) has the minimum sum of 6. After replacement, nums = [5,6].
# The array nums became non-decreasing in two operations.

# Example 2:

# Input: nums = [1,2,2]

# Output: 0

# Explanation:

# The array nums is already sorted.

 

# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109



n = [5,2,3,1]
n = [1,2,2]

def xyz(nums):
    N = len(nums)
    if N < 2:
        return 0
    
    array = [int(x) for x in nums]
    left = list(range(-1, N - 1))
    right = list(range(1, N + 1))
    
    flipped = 0
    pairSum = SortedList() # type: ignore
    
    def add(i, N, array):
        nonlocal flipped
        if 0 <= i < N:
            j = right[i]
            if j < N:
                pairSum.add([array[i] + array[j], i])
                if array[i] > array[j]:
                    flipped += 1
                    
    def remove(i, N, array):
        nonlocal flipped
        if 0 <= i < N:
            j = right[i]
            if j < N:
                if array[i] > array[j]:
                    flipped -= 1
                pairSum.discard([array[i] + array[j], i])

    for i in range(N - 1):
        if array[i] > array[i + 1]:
            flipped += 1
        pairSum.add([array[i] + array[i + 1], i])
        
    op = 0
    
    while flipped > 0 and pairSum:
        s, i = pairSum.pop(0)
        
        j = right[i]
        h = left[i]
        k = right[j]
        
        remove(h, N, array)
        if array[i] > array[j]:
            flipped -= 1
        remove(j, N, array)
        
        array[i] += array[j]
        op += 1
        
        right[i] = k
        if k < N:
            left[k] = i
            
        add(h, N, array)
        add(i, N, array)
        
    return op

print(xyz(n))