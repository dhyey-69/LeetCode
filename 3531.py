# 3531. Count Covered Buildings
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are given a positive integer n, representing an n x n city. You are also given a 2D grid buildings, where buildings[i] = [x, y] denotes a unique building located at coordinates [x, y].

# A building is covered if there is at least one building in all four directions: left, right, above, and below.

# Return the number of covered buildings.

 

# Example 1:



# Input: n = 3, buildings = [[1,2],[2,2],[3,2],[2,1],[2,3]]

# Output: 1

# Explanation:

# Only building [2,2] is covered as it has at least one building:
# above ([1,2])
# below ([3,2])
# left ([2,1])
# right ([2,3])
# Thus, the count of covered buildings is 1.
# Example 2:



# Input: n = 3, buildings = [[1,1],[1,2],[2,1],[2,2]]

# Output: 0

# Explanation:

# No building has at least one building in all four directions.
# Example 3:



# Input: n = 5, buildings = [[1,3],[3,2],[3,3],[3,5],[5,3]]

# Output: 1

# Explanation:

# Only building [3,3] is covered as it has at least one building:
# above ([1,3])
# below ([5,3])
# left ([3,2])
# right ([3,5])
# Thus, the count of covered buildings is 1.
 

# Constraints:

# 2 <= n <= 105
# 1 <= buildings.length <= 105 
# buildings[i] = [x, y]
# 1 <= x, y <= n
# All coordinates of buildings are unique.

n = 3
b = [[1,2],[2,2],[3,2],[2,1],[2,3]]

# n = 3
# b = [[1,1],[1,2],[2,1],[2,2]]

# n = 5
# b = [[1,3],[3,2],[3,3],[3,5],[5,3]]

def xyz(n,buildings):
    rows = {}
    cols = {}

    for x, y in buildings:
        if x not in rows:
            rows[x] = []
        if y not in cols:
            cols[y] = []
        rows[x].append(y)
        cols[y].append(x)

    for r in rows:
        rows[r].sort()
    for c in cols:
        cols[c].sort()

    def find_index(arr, target):
        lo, hi = 0, len(arr) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1

    covered = 0
    for x, y in buildings:
        ys = rows[x]
        xs = cols[y]

        iy = find_index(ys, y)
        ix = find_index(xs, x)

        has_left = iy > 0
        has_right = iy < len(ys) - 1
        has_above = ix > 0
        has_below = ix < len(xs) - 1

        if has_left and has_right and has_above and has_below:
            covered += 1

    return covered


print(xyz(n,b))