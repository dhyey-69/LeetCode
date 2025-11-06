# 3607. Power Grid Maintenance
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are given an integer c representing c power stations, each with a unique identifier id from 1 to c (1‑based indexing).

# These stations are interconnected via n bidirectional cables, represented by a 2D array connections, where each element connections[i] = [ui, vi] indicates a connection between station ui and station vi. Stations that are directly or indirectly connected form a power grid.

# Initially, all stations are online (operational).

# You are also given a 2D array queries, where each query is one of the following two types:

# [1, x]: A maintenance check is requested for station x. If station x is online, it resolves the check by itself. If station x is offline, the check is resolved by the operational station with the smallest id in the same power grid as x. If no operational station exists in that grid, return -1.

# [2, x]: Station x goes offline (i.e., it becomes non-operational).

# Return an array of integers representing the results of each query of type [1, x] in the order they appear.

# Note: The power grid preserves its structure; an offline (non‑operational) node remains part of its grid and taking it offline does not alter connectivity.

 

# Example 1:

# Input: c = 5, connections = [[1,2],[2,3],[3,4],[4,5]], queries = [[1,3],[2,1],[1,1],[2,2],[1,2]]

# Output: [3,2,3]

# Explanation:



# Initially, all stations {1, 2, 3, 4, 5} are online and form a single power grid.
# Query [1,3]: Station 3 is online, so the maintenance check is resolved by station 3.
# Query [2,1]: Station 1 goes offline. The remaining online stations are {2, 3, 4, 5}.
# Query [1,1]: Station 1 is offline, so the check is resolved by the operational station with the smallest id among {2, 3, 4, 5}, which is station 2.
# Query [2,2]: Station 2 goes offline. The remaining online stations are {3, 4, 5}.
# Query [1,2]: Station 2 is offline, so the check is resolved by the operational station with the smallest id among {3, 4, 5}, which is station 3.
# Example 2:

# Input: c = 3, connections = [], queries = [[1,1],[2,1],[1,1]]

# Output: [1,-1]

# Explanation:

# There are no connections, so each station is its own isolated grid.
# Query [1,1]: Station 1 is online in its isolated grid, so the maintenance check is resolved by station 1.
# Query [2,1]: Station 1 goes offline.
# Query [1,1]: Station 1 is offline and there are no other stations in its grid, so the result is -1.
 

# Constraints:

# 1 <= c <= 105
# 0 <= n == connections.length <= min(105, c * (c - 1) / 2)
# connections[i].length == 2
# 1 <= ui, vi <= c
# ui != vi
# 1 <= queries.length <= 2 * 105
# queries[i].length == 2
# queries[i][0] is either 1 or 2.
# 1 <= queries[i][1] <= c

c = 5
con = [[1,2],[2,3],[3,4],[4,5]]
q = [[1,3],[2,1],[1,1],[2,2],[1,2]]

# c = 3
# con = []
# q = [[1,1],[2,1],[1,1]]

def xyz(c,connections,queries):
    parent = [i for i in range(c + 1)]
    rank = [0] * (c + 1)
    
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(x, y):
        xr, yr = find(x), find(y)
        if xr == yr:
            return
        if rank[xr] < rank[yr]:
            parent[xr] = yr
        elif rank[xr] > rank[yr]:
            parent[yr] = xr
        else:
            parent[yr] = xr
            rank[xr] += 1

    for u, v in connections:
        union(u, v)

    comps = {}
    for i in range(1, c + 1):
        r = find(i)
        if r not in comps:
            comps[r] = []
        comps[r].append(i)
    for r in comps:
        comps[r].sort()

    offline = [False] * (c + 1)
    min_online = {}
    for r, arr in comps.items():
        min_online[r] = arr[0]

    res = []

    for typ, x in queries:
        if typ == 1:
            if not offline[x]:
                res.append(x)
            else:
                r = find(x)
                curr_min = min_online[r]
                if offline[curr_min]:
                    arr = comps[r]
                    idx = 0
                    while idx < len(arr) and offline[arr[idx]]:
                        idx += 1
                    if idx < len(arr):
                        min_online[r] = arr[idx]
                        curr_min = arr[idx]
                    else:
                        min_online[r] = -1
                        curr_min = -1
                res.append(curr_min)
        else:
            offline[x] = True
            r = find(x)
            if min_online[r] == x:
                pass

    return res


print(xyz(c,con,q))