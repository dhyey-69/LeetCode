# 3625. Count Number of Trapezoids II
# Hard
# Topics
# premium lock icon
# Companies
# Hint
# You are given a 2D integer array points where points[i] = [xi, yi] represents the coordinates of the ith point on the Cartesian plane.

# Return the number of unique trapezoids that can be formed by choosing any four distinct points from points.

# A trapezoid is a convex quadrilateral with at least one pair of parallel sides. Two lines are parallel if and only if they have the same slope.

 

# Example 1:

# Input: points = [[-3,2],[3,0],[2,3],[3,2],[2,-3]]

# Output: 2

# Explanation:



# There are two distinct ways to pick four points that form a trapezoid:

# The points [-3,2], [2,3], [3,2], [2,-3] form one trapezoid.
# The points [2,3], [3,2], [3,0], [2,-3] form another trapezoid.
# Example 2:

# Input: points = [[0,0],[1,0],[0,1],[2,1]]

# Output: 1

# Explanation:



# There is only one trapezoid which can be formed.

 

# Constraints:

# 4 <= points.length <= 500
# –1000 <= xi, yi <= 1000
# All points are pairwise distinct.


p = [[-3,2],[3,0],[2,3],[3,2],[2,-3]]
# p = [[0,0],[1,0],[0,1],[2,1]]

def xyz(points):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a if a >= 0 else -a

    n = len(points)
    slope_map = {}
    for i in range(n):
        x1, y1 = points[i]
        for j in range(i + 1, n):
            x2, y2 = points[j]
            dy, dx = y2 - y1, x2 - x1
            if dx == 0:
                key = (1, 0)
                line_key = (1, 0, x1)
            elif dy == 0:
                key = (0, 1)
                line_key = (0, 1, -y1)
            else:
                g = gcd(dy, dx)
                dy //= g
                dx //= g
                if dx < 0:
                    dx = -dx
                    dy = -dy
                key = (dy, dx)
                line_key = (dy, dx, dy * x1 - dx * y1)
            if key not in slope_map:
                slope_map[key] = []
            slope_map[key].append((i, j, line_key))

    total = 0
    for segs in slope_map.values():
        k = len(segs)
        if k < 2:
            continue
        total_pairs = k * (k - 1) // 2
        deg = {}
        for a, b, _ in segs:
            deg[a] = deg.get(a, 0) + 1
            deg[b] = deg.get(b, 0) + 1
        pairs_share = 0
        for d in deg.values():
            pairs_share += d * (d - 1) // 2
        line_count = {}
        for _, _, lk in segs:
            line_count[lk] = line_count.get(lk, 0) + 1
        pairs_same_line = 0
        for c in line_count.values():
            pairs_same_line += c * (c - 1) // 2
        deg_line = {}
        for a, b, lk in segs:
            if a not in deg_line:
                deg_line[a] = {}
            if b not in deg_line:
                deg_line[b] = {}
            deg_line[a][lk] = deg_line[a].get(lk, 0) + 1
            deg_line[b][lk] = deg_line[b].get(lk, 0) + 1
        pairs_both = 0
        for p in deg_line:
            for c in deg_line[p].values():
                pairs_both += c * (c - 1) // 2
        contrib = total_pairs - pairs_share - pairs_same_line + pairs_both
        total += contrib

    mid_map = {}
    for i in range(n):
        x1, y1 = points[i]
        for j in range(i + 1, n):
            x2, y2 = points[j]
            mid = (x1 + x2, y1 + y2)
            dy, dx = y2 - y1, x2 - x1
            if dx == 0:
                line_id = (1, 0, x1)
            elif dy == 0:
                line_id = (0, 1, -y1)
            else:
                g = gcd(dy, dx)
                dy //= g
                dx //= g
                if dx < 0:
                    dx = -dx
                    dy = -dy
                line_id = (dy, dx, dy * x1 - dx * y1)
            if mid not in mid_map:
                mid_map[mid] = []
            mid_map[mid].append(line_id)

    parallelograms = 0
    for lst in mid_map.values():
        m = len(lst)
        if m < 2:
            continue
        total_pairs = m * (m - 1) // 2
        line_count = {}
        for lid in lst:
            line_count[lid] = line_count.get(lid, 0) + 1
        bad = 0
        for c in line_count.values():
            bad += c * (c - 1) // 2
        parallelograms += total_pairs - bad

    return total - parallelograms

print(xyz(p))