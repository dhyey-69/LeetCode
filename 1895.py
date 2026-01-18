# 1895. Largest Magic Square
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# A k x k magic square is a k x k grid filled with integers such that every row sum, every column sum, and both diagonal sums are all equal. The integers in the magic square do not have to be distinct. Every 1 x 1 grid is trivially a magic square.

# Given an m x n integer grid, return the size (i.e., the side length k) of the largest magic square that can be found within this grid.

 

# Example 1:


# Input: grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]
# Output: 3
# Explanation: The largest magic square has a size of 3.
# Every row sum, column sum, and diagonal sum of this magic square is equal to 12.
# - Row sums: 5+1+6 = 5+4+3 = 2+7+3 = 12
# - Column sums: 5+5+2 = 1+4+7 = 6+3+3 = 12
# - Diagonal sums: 5+4+3 = 6+4+2 = 12
# Example 2:


# Input: grid = [[5,1,3,1],[9,3,3,1],[1,3,3,8]]
# Output: 2
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# 1 <= grid[i][j] <= 106



g = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]
# g = [[5,1,3,1],[9,3,3,1],[1,3,3,8]]

def xyz(grid):
    m, n = len(grid), len(grid[0])
        
    row = [[0]*(n+1) for _ in range(m)]
    col = [[0]*n for _ in range(m+1)]
    diag1 = [[0]*(n+1) for _ in range(m+1)]
    diag2 = [[0]*(n+2) for _ in range(m+1)]
    
    for i in range(m):
        for j in range(n):
            row[i][j+1] = row[i][j] + grid[i][j]
            col[i+1][j] = col[i][j] + grid[i][j]
            diag1[i+1][j+1] = diag1[i][j] + grid[i][j]
            diag2[i+1][j] = diag2[i][j+1] + grid[i][j]

    def is_magic(x, y, k):
        target = row[x][y+k] - row[x][y]
        
        for i in range(x, x+k):
            if row[i][y+k] - row[i][y] != target:
                return False
        
        for j in range(y, y+k):
            if col[x+k][j] - col[x][j] != target:
                return False
        
        if diag1[x+k][y+k] - diag1[x][y] != target:
            return False
        if diag2[x+k][y] - diag2[x][y+k] != target:
            return False
        
        return True

    for k in range(min(m, n), 1, -1):
        for i in range(m - k + 1):
            for j in range(n - k + 1):
                if is_magic(i, j, k):
                    return k
    
    return 1


print(xyz(g))