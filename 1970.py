# 1970. Last Day Where You Can Still Cross
# Hard
# Topics
# premium lock icon
# Companies
# Hint
# There is a 1-based binary matrix where 0 represents land and 1 represents water. You are given integers row and col representing the number of rows and columns in the matrix, respectively.

# Initially on day 0, the entire matrix is land. However, each day a new cell becomes flooded with water. You are given a 1-based 2D array cells, where cells[i] = [ri, ci] represents that on the ith day, the cell on the rith row and cith column (1-based coordinates) will be covered with water (i.e., changed to 1).

# You want to find the last day that it is possible to walk from the top to the bottom by only walking on land cells. You can start from any cell in the top row and end at any cell in the bottom row. You can only travel in the four cardinal directions (left, right, up, and down).

# Return the last day where it is possible to walk from the top to the bottom by only walking on land cells.

 

# Example 1:


# Input: row = 2, col = 2, cells = [[1,1],[2,1],[1,2],[2,2]]
# Output: 2
# Explanation: The above image depicts how the matrix changes each day starting from day 0.
# The last day where it is possible to cross from top to bottom is on day 2.
# Example 2:


# Input: row = 2, col = 2, cells = [[1,1],[1,2],[2,1],[2,2]]
# Output: 1
# Explanation: The above image depicts how the matrix changes each day starting from day 0.
# The last day where it is possible to cross from top to bottom is on day 1.
# Example 3:


# Input: row = 3, col = 3, cells = [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]
# Output: 3
# Explanation: The above image depicts how the matrix changes each day starting from day 0.
# The last day where it is possible to cross from top to bottom is on day 3.
 

# Constraints:

# 2 <= row, col <= 2 * 104
# 4 <= row * col <= 2 * 104
# cells.length == row * col
# 1 <= ri <= row
# 1 <= ci <= col
# All the values of cells are unique.



row = 2
col = 2
c = [[1,1],[2,1],[1,2],[2,2]]

# row = 2
# col = 2
# c = [[1,1],[1,2],[2,1],[2,2]]

# row = 3
# col = 3
# c = [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]

def xyz(row,col,cells):
    n = row * col
    
    parent = list(range(n + 2))
    size = [1] * (n + 2)
    TOP = n
    BOTTOM = n + 1
    
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(a, b):
        pa, pb = find(a), find(b)
        if pa == pb:
            return
        if size[pa] < size[pb]:
            pa, pb = pb, pa
        parent[pb] = pa
        size[pa] += size[pb]
    
    grid = [[0] * col for _ in range(row)]
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    
    for day in range(len(cells) - 1, -1, -1):
        r, c = cells[day]
        r -= 1
        c -= 1
        grid[r][c] = 1
        idx = r * col + c
        
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
                union(idx, nr * col + nc)
        
        if r == 0:
            union(idx, TOP)
        if r == row - 1:
            union(idx, BOTTOM)
        
        if find(TOP) == find(BOTTOM):
            return day
    
    return 0

print(xyz(row,col,c))