# 2322. Minimum Score After Removals on a Tree
# Hard
# Topics
# premium lock icon
# Companies
# Hint
# There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

# You are given a 0-indexed integer array nums of length n where nums[i] represents the value of the ith node. You are also given a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

# Remove two distinct edges of the tree to form three connected components. For a pair of removed edges, the following steps are defined:

# Get the XOR of all the values of the nodes for each of the three components respectively.
# The difference between the largest XOR value and the smallest XOR value is the score of the pair.
# For example, say the three components have the node values: [4,5,7], [1,9], and [3,3,3]. The three XOR values are 4 ^ 5 ^ 7 = 6, 1 ^ 9 = 8, and 3 ^ 3 ^ 3 = 3. The largest XOR value is 8 and the smallest XOR value is 3. The score is then 8 - 3 = 5.
# Return the minimum score of any possible pair of edge removals on the given tree.

 

# Example 1:


# Input: nums = [1,5,5,4,11], edges = [[0,1],[1,2],[1,3],[3,4]]
# Output: 9
# Explanation: The diagram above shows a way to make a pair of removals.
# - The 1st component has nodes [1,3,4] with values [5,4,11]. Its XOR value is 5 ^ 4 ^ 11 = 10.
# - The 2nd component has node [0] with value [1]. Its XOR value is 1 = 1.
# - The 3rd component has node [2] with value [5]. Its XOR value is 5 = 5.
# The score is the difference between the largest and smallest XOR value which is 10 - 1 = 9.
# It can be shown that no other pair of removals will obtain a smaller score than 9.
# Example 2:


# Input: nums = [5,5,2,4,4,2], edges = [[0,1],[1,2],[5,2],[4,3],[1,3]]
# Output: 0
# Explanation: The diagram above shows a way to make a pair of removals.
# - The 1st component has nodes [3,4] with values [4,4]. Its XOR value is 4 ^ 4 = 0.
# - The 2nd component has nodes [1,0] with values [5,5]. Its XOR value is 5 ^ 5 = 0.
# - The 3rd component has nodes [2,5] with values [2,2]. Its XOR value is 2 ^ 2 = 0.
# The score is the difference between the largest and smallest XOR value which is 0 - 0 = 0.
# We cannot obtain a smaller score than 0.
 

# Constraints:

# n == nums.length
# 3 <= n <= 1000
# 1 <= nums[i] <= 108
# edges.length == n - 1
# edges[i].length == 2
# 0 <= ai, bi < n
# ai != bi
# edges represents a valid tree.

n = [1,5,5,4,11]
e = [[0,1],[1,2],[1,3],[3,4]]

n = [5,5,2,4,4,2]
e = [[0,1],[1,2],[5,2],[4,3],[1,3]]

def xyz(nums,edges):
    n = len(nums)
        
    tree = [[] for _ in range(n)]
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    xor_subtree = [0] * n
    parent = [-1] * n
    tin = [0] * n
    tout = [0] * n
    time = [1]

    def dfs(node, par):
        parent[node] = par
        tin[node] = time[0]
        time[0] += 1
        total = nums[node]
        for nei in tree[node]:
            if nei != par:
                total ^= dfs(nei, node)
        xor_subtree[node] = total
        tout[node] = time[0]
        time[0] += 1
        return total

    dfs(0, -1)
    total_xor = xor_subtree[0]

    edge_nodes = []
    for u, v in edges:
        if parent[u] == v:
            edge_nodes.append((u, v))
        else:
            edge_nodes.append((v, u))

    res = float('inf')

    def is_ancestor(u, v):
        return tin[u] < tin[v] and tout[v] < tout[u]

    for i in range(len(edge_nodes)):
        for j in range(i + 1, len(edge_nodes)):
            a, _ = edge_nodes[i]
            b, _ = edge_nodes[j]

            if is_ancestor(a, b):
                x = xor_subtree[b]
                y = xor_subtree[a] ^ xor_subtree[b]
                z = total_xor ^ xor_subtree[a]
            elif is_ancestor(b, a):
                x = xor_subtree[a]
                y = xor_subtree[b] ^ xor_subtree[a]
                z = total_xor ^ xor_subtree[b]
            else:
                x = xor_subtree[a]
                y = xor_subtree[b]
                z = total_xor ^ x ^ y

            res = min(res, max(x, y, z) - min(x, y, z))

    return res

print(xyz(n,e))