# 3623. Count Number of Trapezoids I
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are given a 2D integer array points, where points[i] = [xi, yi] represents the coordinates of the ith point on the Cartesian plane.

# A horizontal trapezoid is a convex quadrilateral with at least one pair of horizontal sides (i.e. parallel to the x-axis). Two lines are parallel if and only if they have the same slope.

# Return the number of unique horizontal trapezoids that can be formed by choosing any four distinct points from points.

# Since the answer may be very large, return it modulo 109 + 7.

 

# Example 1:

# Input: points = [[1,0],[2,0],[3,0],[2,2],[3,2]]

# Output: 3

# Explanation:



# There are three distinct ways to pick four points that form a horizontal trapezoid:

# Using points [1,0], [2,0], [3,2], and [2,2].
# Using points [2,0], [3,0], [3,2], and [2,2].
# Using points [1,0], [3,0], [3,2], and [2,2].
# Example 2:

# Input: points = [[0,0],[1,0],[0,1],[2,1]]

# Output: 1

# Explanation:



# There is only one horizontal trapezoid that can be formed.

 

# Constraints:

# 4 <= points.length <= 105
# –108 <= xi, yi <= 108
# All points are pairwise distinct.



p = [[1,0],[2,0],[3,0],[2,2],[3,2]]
# p = [[0,0],[1,0],[0,1],[2,1]]

def xyz(points):
    MOD = 10**9 + 7

    ycount = {}
    for x, y in points:
        if y in ycount:
            ycount[y] += 1
        else:
            ycount[y] = 1

    hs = []
    for k in ycount.values():
        if k >= 2:
            hs.append(k * (k - 1) // 2)

    n = len(hs)
    if n < 2:
        return 0

    total_h = 0
    total_h_sq = 0
    for h in hs:
        total_h = (total_h + h) % MOD
        total_h_sq = (total_h_sq + (h * h) % MOD) % MOD

    ans = (total_h * total_h - total_h_sq) % MOD

    inv2 = (MOD + 1) // 2
    ans = (ans * inv2) % MOD

    return ans


print(xyz(p))