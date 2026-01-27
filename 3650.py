# 3650. Minimum Cost Path with Edge Reversals
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are given a directed, weighted graph with n nodes labeled from 0 to n - 1, and an array edges where edges[i] = [ui, vi, wi] represents a directed edge from node ui to node vi with cost wi.

# Each node ui has a switch that can be used at most once: when you arrive at ui and have not yet used its switch, you may activate it on one of its incoming edges vi → ui reverse that edge to ui → vi and immediately traverse it.

# The reversal is only valid for that single move, and using a reversed edge costs 2 * wi.

# Return the minimum total cost to travel from node 0 to node n - 1. If it is not possible, return -1.

 

# Example 1:

# Input: n = 4, edges = [[0,1,3],[3,1,1],[2,3,4],[0,2,2]]

# Output: 5

# Explanation:



# Use the path 0 → 1 (cost 3).
# At node 1 reverse the original edge 3 → 1 into 1 → 3 and traverse it at cost 2 * 1 = 2.
# Total cost is 3 + 2 = 5.
# Example 2:

# Input: n = 4, edges = [[0,2,1],[2,1,1],[1,3,1],[2,3,3]]

# Output: 3

# Explanation:

# No reversal is needed. Take the path 0 → 2 (cost 1), then 2 → 1 (cost 1), then 1 → 3 (cost 1).
# Total cost is 1 + 1 + 1 = 3.
 

# Constraints:

# 2 <= n <= 5 * 104
# 1 <= edges.length <= 105
# edges[i] = [ui, vi, wi]
# 0 <= ui, vi <= n - 1
# 1 <= wi <= 1000

n = 4
e = [[0,1,3],[3,1,1],[2,3,4],[0,2,2]]

# n = 4
# e = [[0,2,1],[2,1,1],[1,3,1],[2,3,3]]

def xyz(n,edges):
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, 2 * w))

    INF = 10**30
    dist = [INF] * n
    dist[0] = 0

    heap = []

    def heappush(item):
        heap.append(item)
        i = len(heap) - 1
        while i > 0:
            p = (i - 1) // 2
            if heap[p][0] <= heap[i][0]:
                break
            heap[p], heap[i] = heap[i], heap[p]
            i = p

    def heappop():
        root = heap[0]
        last = heap.pop()
        if heap:
            heap[0] = last
            i = 0
            size = len(heap)
            while True:
                l = 2 * i + 1
                r = l + 1
                smallest = i

                if l < size and heap[l][0] < heap[smallest][0]:
                    smallest = l
                if r < size and heap[r][0] < heap[smallest][0]:
                    smallest = r

                if smallest == i:
                    break
                heap[i], heap[smallest] = heap[smallest], heap[i]
                i = smallest
        return root

    heappush((0, 0))

    while heap:
        cost, u = heappop()
        if cost > dist[u]:
            continue
        if u == n - 1:
            return cost

        for v, w in graph[u]:
            nc = cost + w
            if nc < dist[v]:
                dist[v] = nc
                heappush((nc, v))

    return -1


print(xyz(n,e))