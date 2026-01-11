# 85. Maximal Rectangle
# Hard
# Topics
# premium lock icon
# Companies
# Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

 

# Example 1:


# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 6
# Explanation: The maximal rectangle is shown in the above picture.
# Example 2:

# Input: matrix = [["0"]]
# Output: 0
# Example 3:

# Input: matrix = [["1"]]
# Output: 1
 

# Constraints:

# rows == matrix.length
# cols == matrix[i].length
# 1 <= rows, cols <= 200
# matrix[i][j] is '0' or '1'.



m = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# m = [["0"]]
# m = [["1"]]

def xyz(matrix):
    if not matrix:
        return 0
    
    rows, cols = len(matrix), len(matrix[0])
    heights = [0] * cols
    best = 0

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == '1':
                heights[c] += 1
            else:
                heights[c] = 0
        
        stack = []
        for i in range(cols + 1):
            h = heights[i] if i < cols else 0
            while stack and h < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                best = max(best, height * width)
            stack.append(i)

    return best

print(xyz(m))