# 2040. Kth Smallest Product of Two Sorted Arrays
# Hard
# Topics
# premium lock icon
# Companies
# Hint
# Given two sorted 0-indexed integer arrays nums1 and nums2 as well as an integer k, return the kth (1-based) smallest product of nums1[i] * nums2[j] where 0 <= i < nums1.length and 0 <= j < nums2.length.
 

# Example 1:

# Input: nums1 = [2,5], nums2 = [3,4], k = 2
# Output: 8
# Explanation: The 2 smallest products are:
# - nums1[0] * nums2[0] = 2 * 3 = 6
# - nums1[0] * nums2[1] = 2 * 4 = 8
# The 2nd smallest product is 8.
# Example 2:

# Input: nums1 = [-4,-2,0,3], nums2 = [2,4], k = 6
# Output: 0
# Explanation: The 6 smallest products are:
# - nums1[0] * nums2[1] = (-4) * 4 = -16
# - nums1[0] * nums2[0] = (-4) * 2 = -8
# - nums1[1] * nums2[1] = (-2) * 4 = -8
# - nums1[1] * nums2[0] = (-2) * 2 = -4
# - nums1[2] * nums2[0] = 0 * 2 = 0
# - nums1[2] * nums2[1] = 0 * 4 = 0
# The 6th smallest product is 0.
# Example 3:

# Input: nums1 = [-2,-1,0,1,2], nums2 = [-3,-1,2,4,5], k = 3
# Output: -6
# Explanation: The 3 smallest products are:
# - nums1[0] * nums2[4] = (-2) * 5 = -10
# - nums1[0] * nums2[3] = (-2) * 4 = -8
# - nums1[4] * nums2[0] = 2 * (-3) = -6
# The 3rd smallest product is -6.
 

# Constraints:

# 1 <= nums1.length, nums2.length <= 5 * 104
# -105 <= nums1[i], nums2[j] <= 105
# 1 <= k <= nums1.length * nums2.length
# nums1 and nums2 are sorted.


n1 = [2,5]
n2 = [3,4]
k = 2

# n1 = [-4,-2,0,3]
# n2 = [2,4]
# k = 6

# n1 = [-2,-1,0,1,2]
# n2 = [-3,-1,2,4,5]
# k = 3

def xyz(nums1,nums2,k):
    def separate(A):
        A1 = []
        A2 = []
        for a in A:
            if a < 0:
                A1.append(-a)
            else:
                A2.append(a)
        A1.reverse()
        return A1, A2

    def numProductNoGreaterThan(A, B, m):
        count = 0
        j = len(B) - 1
        for a in A:
            while j >= 0 and a * B[j] > m:
                j -= 1
            count += j + 1
        return count

    A1, A2 = separate(nums1)
    B1, B2 = separate(nums2)

    negCount = len(A1) * len(B2) + len(A2) * len(B1)
    sign = 1

    if k > negCount:
        k -= negCount
    else:
        k = negCount - k + 1
        sign = -1
        B1, B2 = B2, B1

    l, r = 0, int(1e10)

    while l < r:
        m = (l + r) // 2
        if numProductNoGreaterThan(A1, B1, m) + numProductNoGreaterThan(A2, B2, m) >= k:
            r = m
        else:
            l = m + 1

    return sign * l

print(xyz(n1,n2,k))