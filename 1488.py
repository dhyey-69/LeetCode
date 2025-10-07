# 1488. Avoid Flood in The City
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Your country has an infinite number of lakes. Initially, all the lakes are empty, but when it rains over the nth lake, the nth lake becomes full of water. If it rains over a lake that is full of water, there will be a flood. Your goal is to avoid floods in any lake.

# Given an integer array rains where:

# rains[i] > 0 means there will be rains over the rains[i] lake.
# rains[i] == 0 means there are no rains this day and you can choose one lake this day and dry it.
# Return an array ans where:

# ans.length == rains.length
# ans[i] == -1 if rains[i] > 0.
# ans[i] is the lake you choose to dry in the ith day if rains[i] == 0.
# If there are multiple valid answers return any of them. If it is impossible to avoid flood return an empty array.

# Notice that if you chose to dry a full lake, it becomes empty, but if you chose to dry an empty lake, nothing changes.

 

# Example 1:

# Input: rains = [1,2,3,4]
# Output: [-1,-1,-1,-1]
# Explanation: After the first day full lakes are [1]
# After the second day full lakes are [1,2]
# After the third day full lakes are [1,2,3]
# After the fourth day full lakes are [1,2,3,4]
# There's no day to dry any lake and there is no flood in any lake.
# Example 2:

# Input: rains = [1,2,0,0,2,1]
# Output: [-1,-1,2,1,-1,-1]
# Explanation: After the first day full lakes are [1]
# After the second day full lakes are [1,2]
# After the third day, we dry lake 2. Full lakes are [1]
# After the fourth day, we dry lake 1. There is no full lakes.
# After the fifth day, full lakes are [2].
# After the sixth day, full lakes are [1,2].
# It is easy that this scenario is flood-free. [-1,-1,1,2,-1,-1] is another acceptable scenario.
# Example 3:

# Input: rains = [1,2,0,1,2]
# Output: []
# Explanation: After the second day, full lakes are  [1,2]. We have to dry one lake in the third day.
# After that, it will rain over lakes [1,2]. It's easy to prove that no matter which lake you choose to dry in the 3rd day, the other one will flood.
 

# Constraints:

# 1 <= rains.length <= 105
# 0 <= rains[i] <= 109


r = [1,2,3,4]
# r = [1,2,0,0,2,1]

def xyz(rains):
    def heappush(heap, item):
        heap.append(item)
        i = len(heap) - 1
        while i > 0:
            parent = (i - 1) // 2
            if heap[parent][0] <= heap[i][0]:
                break
            heap[parent], heap[i] = heap[i], heap[parent]
            i = parent

    def heappop(heap):
        if not heap:
            return None
        smallest = heap[0]
        last = heap.pop()
        if heap:
            heap[0] = last
            i = 0
            n = len(heap)
            while True:
                left, right = 2 * i + 1, 2 * i + 2
                smallest_i = i
                if left < n and heap[left][0] < heap[smallest_i][0]:
                    smallest_i = left
                if right < n and heap[right][0] < heap[smallest_i][0]:
                    smallest_i = right
                if smallest_i == i:
                    break
                heap[i], heap[smallest_i] = heap[smallest_i], heap[i]
                i = smallest_i
        return smallest

    n = len(rains)
    ans = [-1] * n

    next_rains = {}
    for i in range(n - 1, -1, -1):
        lake = rains[i]
        if lake > 0:
            if lake not in next_rains:
                next_rains[lake] = []
            next_rains[lake].append(i)

    full = set()
    heap = []

    for i in range(n):
        lake = rains[i]
        if lake > 0:
            next_rains[lake].pop()
            if lake in full:
                return []
            full.add(lake)
            if next_rains[lake]:
                next_idx = next_rains[lake][-1]
                heappush(heap, (next_idx, lake))
            ans[i] = -1
        else:
            if heap:
                _, dry_lake = heappop(heap)
                full.remove(dry_lake)
                ans[i] = dry_lake
            else:
                ans[i] = 1

    return ans

    
print(xyz(r))