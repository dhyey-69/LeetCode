# 1504. Count Submatrices With All Ones
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given an m x n binary matrix mat, return the number of submatrices that have all ones.

 

# Example 1:


# Input: mat = [[1,0,1],[1,1,0],[1,1,0]]
# Output: 13
# Explanation: 
# There are 6 rectangles of side 1x1.
# There are 2 rectangles of side 1x2.
# There are 3 rectangles of side 2x1.
# There is 1 rectangle of side 2x2. 
# There is 1 rectangle of side 3x1.
# Total number of rectangles = 6 + 2 + 3 + 1 + 1 = 13.
# Example 2:


# Input: mat = [[0,1,1,0],[0,1,1,1],[1,1,1,0]]
# Output: 24
# Explanation: 
# There are 8 rectangles of side 1x1.
# There are 5 rectangles of side 1x2.
# There are 2 rectangles of side 1x3. 
# There are 4 rectangles of side 2x1.
# There are 2 rectangles of side 2x2. 
# There are 2 rectangles of side 3x1. 
# There is 1 rectangle of side 3x2. 
# Total number of rectangles = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24.
 

# Constraints:

# 1 <= m, n <= 150
# mat[i][j] is either 0 or 1.


m = [[1,0,1],[1,1,0],[1,1,0]]
# m = [[0,1,1,0],[0,1,1,1],[1,1,1,0]]

def xyz(mat):
    m, n = len(mat), len(mat[0])
    heights = [0] * n
    res = 0

    for i in range(m):
        for j in range(n):
            if mat[i][j] == 1:
                heights[j] += 1
            else:
                heights[j] = 0

        for j in range(n):
            min_height = heights[j]
            for k in range(j, -1, -1):
                if heights[k] == 0:
                    break
                min_height = min(min_height, heights[k])
                res += min_height

    return res

print(xyz(m))