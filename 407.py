# 407. Trapping Rain Water II
# Hard
# Topics
# premium lock icon
# Companies
# Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map, return the volume of water it can trap after raining.

 

# Example 1:


# Input: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
# Output: 4
# Explanation: After the rain, water is trapped between the blocks.
# We have two small ponds 1 and 3 units trapped.
# The total volume of water trapped is 4.
# Example 2:


# Input: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
# Output: 10
 

# Constraints:

# m == heightMap.length
# n == heightMap[i].length
# 1 <= m, n <= 200
# 0 <= heightMap[i][j] <= 2 * 104


hm = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
# hm = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]

def xyz(heightMap):
    if not heightMap or not heightMap[0]:
        return 0
    
    m, n = len(heightMap), len(heightMap[0])
    visited = [[False]*n for _ in range(m)]
    heap = []

    for i in range(m):
        for j in range(n):
            if i == 0 or i == m-1 or j == 0 or j == n-1:
                heap.append([heightMap[i][j], i, j])
                visited[i][j] = True
    
    res = 0
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    
    while heap:
        min_index = 0
        for k in range(len(heap)):
            if heap[k][0] < heap[min_index][0]:
                min_index = k
        height, x, y = heap.pop(min_index)

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                res += max(0, height - heightMap[nx][ny])
                heap.append([max(heightMap[nx][ny], height), nx, ny])
    
    return res


print(xyz(hm))