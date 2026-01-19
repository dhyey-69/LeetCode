# 1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given a m x n matrix mat and an integer threshold, return the maximum side-length of a square with a sum less than or equal to threshold or return 0 if there is no such square.

 

# Example 1:


# Input: mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
# Output: 2
# Explanation: The maximum side length of square with sum less than 4 is 2 as shown.
# Example 2:

# Input: mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1
# Output: 0
 

# Constraints:

# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 300
# 0 <= mat[i][j] <= 104
# 0 <= threshold <= 105




m = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]]
t = 4

# m = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]]
# t = 1

def xyz(mat,threshold):
    m, n = len(mat), len(mat[0])

    pre = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m):
        for j in range(n):
            pre[i + 1][j + 1] = (
                mat[i][j]
                + pre[i][j + 1]
                + pre[i + 1][j]
                - pre[i][j]
            )

    def exists_square(k: int) -> bool:
        for i in range(m - k + 1):
            for j in range(n - k + 1):
                s = (
                    pre[i + k][j + k]
                    - pre[i][j + k]
                    - pre[i + k][j]
                    + pre[i][j]
                )
                if s <= threshold:
                    return True
        return False

    left, right = 0, min(m, n)
    while left < right:
        mid = (left + right + 1) // 2
        if exists_square(mid):
            left = mid
        else:
            right = mid - 1

    return left

print(xyz(m,t))