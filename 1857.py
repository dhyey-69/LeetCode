# 1857. Largest Color Value in a Directed Graph
# Hard
# Topics
# Companies
# Hint
# There is a directed graph of n colored nodes and m edges. The nodes are numbered from 0 to n - 1.

# You are given a string colors where colors[i] is a lowercase English letter representing the color of the ith node in this graph (0-indexed). You are also given a 2D array edges where edges[j] = [aj, bj] indicates that there is a directed edge from node aj to node bj.

# A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ... -> xk such that there is a directed edge from xi to xi+1 for every 1 <= i < k. The color value of the path is the number of nodes that are colored the most frequently occurring color along that path.

# Return the largest color value of any valid path in the given graph, or -1 if the graph contains a cycle.

 

# Example 1:



# Input: colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]
# Output: 3
# Explanation: The path 0 -> 2 -> 3 -> 4 contains 3 nodes that are colored "a" (red in the above image).
# Example 2:



# Input: colors = "a", edges = [[0,0]]
# Output: -1
# Explanation: There is a cycle from 0 to 0.
 

# Constraints:

# n == colors.length
# m == edges.length
# 1 <= n <= 105
# 0 <= m <= 105
# colors consists of lowercase English letters.
# 0 <= aj, bj < n

c = "abaca"
e = [[0,1],[0,2],[2,3],[3,4]]

# c = "a"
# e = [[0,0]]

def xyz(colors,edges):
    n = len(colors)
        
    graph = [[] for _ in range(n)]
    indegree = [0] * n
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1
    
    queue = []
    for i in range(n):
        if indegree[i] == 0:
            queue.append(i)
    
    dp = [[0] * 26 for _ in range(n)]
    for i in range(n):
        dp[i][ord(colors[i]) - ord('a')] = 1

    visited = 0
    max_color_val = 0
    front = 0

    while front < len(queue):
        node = queue[front]
        front += 1
        visited += 1

        for neighbor in graph[node]:
            for c in range(26):
                new_val = dp[node][c] + (1 if c == ord(colors[neighbor]) - ord('a') else 0)
                if new_val > dp[neighbor][c]:
                    dp[neighbor][c] = new_val
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

        max_color_val = max(max_color_val, max(dp[node]))

    return max_color_val if visited == n else -1

print(xyz(c,e))