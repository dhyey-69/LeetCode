# 2179. Count Good Triplets in an Array
# Hard
# Topics
# Companies
# Hint
# You are given two 0-indexed arrays nums1 and nums2 of length n, both of which are permutations of [0, 1, ..., n - 1].

# A good triplet is a set of 3 distinct values which are present in increasing order by position both in nums1 and nums2. In other words, if we consider pos1v as the index of the value v in nums1 and pos2v as the index of the value v in nums2, then a good triplet will be a set (x, y, z) where 0 <= x, y, z <= n - 1, such that pos1x < pos1y < pos1z and pos2x < pos2y < pos2z.

# Return the total number of good triplets.

 

# Example 1:

# Input: nums1 = [2,0,1,3], nums2 = [0,1,2,3]
# Output: 1
# Explanation: 
# There are 4 triplets (x,y,z) such that pos1x < pos1y < pos1z. They are (2,0,1), (2,0,3), (2,1,3), and (0,1,3). 
# Out of those triplets, only the triplet (0,1,3) satisfies pos2x < pos2y < pos2z. Hence, there is only 1 good triplet.
# Example 2:

# Input: nums1 = [4,0,1,3,2], nums2 = [4,1,0,2,3]
# Output: 4
# Explanation: The 4 good triplets are (4,0,3), (4,0,2), (4,1,3), and (4,1,2).
 

# Constraints:

# n == nums1.length == nums2.length
# 3 <= n <= 105
# 0 <= nums1[i], nums2[i] <= n - 1
# nums1 and nums2 are permutations of [0, 1, ..., n - 1].

n1 = [2,0,1,3]
n2 = [0,1,2,3]

# n1 = [4,0,1,3,2]
# n2 = [4,1,0,2,3]

def xyz(nums1,nums2):
    n = len(nums1)
        
    pos_in_nums2 = [0] * n
    for i, num in enumerate(nums2):
        pos_in_nums2[num] = i
        
    transformed = [pos_in_nums2[num] for num in nums1]

    def update(bit, index, value):
        index += 1
        while index < len(bit):
            bit[index] += value
            index += index & -index

    def query(bit, index):
        index += 1
        result = 0
        while index > 0:
            result += bit[index]
            index -= index & -index
        return result

    bit = [0] * (n + 2)
    left_smaller = [0] * n
    for i in range(n):
        val = transformed[i]
        left_smaller[i] = query(bit, val - 1)
        update(bit, val, 1)

    bit = [0] * (n + 2)
    right_larger = [0] * n
    for i in reversed(range(n)):
        val = transformed[i]
        right_larger[i] = query(bit, n - 1) - query(bit, val)
        update(bit, val, 1)

    total = 0
    for i in range(n):
        total += left_smaller[i] * right_larger[i]
    return total


print(xyz(n1,n2))