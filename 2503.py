# 2503. Maximum Number of Points From Grid Queries
# Hard
# Topics
# Companies
# Hint
# You are given an m x n integer matrix grid and an array queries of size k.

# Find an array answer of size k such that for each integer queries[i] you start in the top left cell of the matrix and repeat the following process:

# If queries[i] is strictly greater than the value of the current cell that you are in, then you get one point if it is your first time visiting this cell, and you can move to any adjacent cell in all 4 directions: up, down, left, and right.
# Otherwise, you do not get any points, and you end this process.
# After the process, answer[i] is the maximum number of points you can get. Note that for each query you are allowed to visit the same cell multiple times.

# Return the resulting array answer.

 

# Example 1:


# Input: grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,2]
# Output: [5,8,1]
# Explanation: The diagrams above show which cells we visit to get points for each query.
# Example 2:


# Input: grid = [[5,2,1],[1,1,2]], queries = [3]
# Output: [0]
# Explanation: We can not get any points because the value of the top left cell is already greater than or equal to 3.
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 2 <= m, n <= 1000
# 4 <= m * n <= 105
# k == queries.length
# 1 <= k <= 104
# 1 <= grid[i][j], queries[i] <= 106


g = [[1,2,3],[2,5,7],[3,5,1]]
q = [5,6,2]

# g = [[5,2,1],[1,1,2]]
# q = [3]

def xyz(grid, queries):
    m, n = len(grid), len(grid[0])
    sorted_queries = sorted(enumerate(queries), key=lambda x: x[1])
    answer = [0] * len(queries)
        
    visited = [[False] * n for _ in range(m)]
    min_heap = [(grid[0][0], 0, 0)]
    visited[0][0] = True
        
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    cells_visited = 0
        
    def heap_push(heap, value, r, c):
        heap.append((value, r, c))
        i = len(heap) - 1
        while i > 0 and heap[i][0] < heap[(i - 1) // 2][0]:
            heap[i], heap[(i - 1) // 2] = heap[(i - 1) // 2], heap[i]
            i = (i - 1) // 2
        
    def heap_pop(heap):
        if not heap:
            return None
        heap[0], heap[-1] = heap[-1], heap[0]
        value = heap.pop()
        i, size = 0, len(heap)
        while 2 * i + 1 < size:
            j = 2 * i + 1
            if j + 1 < size and heap[j + 1][0] < heap[j][0]:
                j += 1
            if heap[i][0] <= heap[j][0]:
                break
            heap[i], heap[j] = heap[j], heap[i]
            i = j
        return value
        
    for index, query in sorted_queries:
        while min_heap and min_heap[0][0] < query:
            value, r, c = heap_pop(min_heap)
            cells_visited += 1
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    heap_push(min_heap, grid[nr][nc], nr, nc)
                    visited[nr][nc] = True
            
        answer[index] = cells_visited
        
    return answer


print(xyz(g,q))