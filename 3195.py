# 3195. Find the Minimum Area to Cover All Ones I
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are given a 2D binary array grid. Find a rectangle with horizontal and vertical sides with the smallest area, such that all the 1's in grid lie inside this rectangle.

# Return the minimum possible area of the rectangle.

 

# Example 1:

# Input: grid = [[0,1,0],[1,0,1]]

# Output: 6

# Explanation:



# The smallest rectangle has a height of 2 and a width of 3, so it has an area of 2 * 3 = 6.

# Example 2:

# Input: grid = [[1,0],[0,0]]

# Output: 1

# Explanation:



# The smallest rectangle has both height and width 1, so its area is 1 * 1 = 1.

 

# Constraints:

# 1 <= grid.length, grid[i].length <= 1000
# grid[i][j] is either 0 or 1.
# The input is generated such that there is at least one 1 in grid.


g = [[0,1,0],[1,0,1]]
g = [[1,0],[0,0]]

def xyz(grid):
    rows, cols = len(grid), len(grid[0])
        
    min_row, max_row = rows, -1
    min_col, max_col = cols, -1
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                min_row = min(min_row, r)
                max_row = max(max_row, r)
                min_col = min(min_col, c)
                max_col = max(max_col, c)
    
    height = max_row - min_row + 1
    width = max_col - min_col + 1
    
    return height * width

print(xyz(g))