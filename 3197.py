# 3197. Find the Minimum Area to Cover All Ones II
# Hard
# Topics
# premium lock icon
# Companies
# Hint
# You are given a 2D binary array grid. You need to find 3 non-overlapping rectangles having non-zero areas with horizontal and vertical sides such that all the 1's in grid lie inside these rectangles.

# Return the minimum possible sum of the area of these rectangles.

# Note that the rectangles are allowed to touch.

 

# Example 1:

# Input: grid = [[1,0,1],[1,1,1]]

# Output: 5

# Explanation:



# The 1's at (0, 0) and (1, 0) are covered by a rectangle of area 2.
# The 1's at (0, 2) and (1, 2) are covered by a rectangle of area 2.
# The 1 at (1, 1) is covered by a rectangle of area 1.
# Example 2:

# Input: grid = [[1,0,1,0],[0,1,0,1]]

# Output: 5

# Explanation:



# The 1's at (0, 0) and (0, 2) are covered by a rectangle of area 3.
# The 1 at (1, 1) is covered by a rectangle of area 1.
# The 1 at (1, 3) is covered by a rectangle of area 1.
 

# Constraints:

# 1 <= grid.length, grid[i].length <= 30
# grid[i][j] is either 0 or 1.
# The input is generated such that there are at least three 1's in grid.


g = [[1,0,1],[1,1,1]]
# g = [[1,0,1,0],[0,1,0,1]]

def xyz(grid):
    m, n = len(grid), len(grid[0])

    def solve_for_orientation(current_grid):
        gm, gn = len(current_grid), len(current_grid[0])
        ones = [(r, c) for r in range(gm) for c in range(gn) if current_grid[r][c] == 1]

        def get_area(r_start: int, c_start: int, r_end: int, c_end: int) -> float:
            sub_ones = [p for p in ones if r_start <= p[0] < r_end and c_start <= p[1] < c_end]
            if not sub_ones:
                return float('inf')
            
            min_r = min(p[0] for p in sub_ones)
            max_r = max(p[0] for p in sub_ones)
            min_c = min(p[1] for p in sub_ones)
            max_c = max(p[1] for p in sub_ones)
            
            return float((max_r - min_r + 1) * (max_c - min_c + 1))

        min_total_area = float('inf')

        for r1 in range(1, gm - 1):
            for r2 in range(r1 + 1, gm):
                area1 = get_area(0, 0, r1, gn)
                area2 = get_area(r1, 0, r2, gn)
                area3 = get_area(r2, 0, gm, gn)
                min_total_area = min(min_total_area, area1 + area2 + area3)

        for r_cut in range(1, gm):
            area_top = get_area(0, 0, r_cut, gn)
            area_bottom = get_area(r_cut, 0, gm, gn)
            
            for c_cut in range(1, gn):
                area_bottom_left = get_area(r_cut, 0, gm, c_cut)
                area_bottom_right = get_area(r_cut, c_cut, gm, gn)
                min_total_area = min(min_total_area, area_top + area_bottom_left + area_bottom_right)
                
                area_top_left = get_area(0, 0, r_cut, c_cut)
                area_top_right = get_area(0, c_cut, r_cut, gn)
                min_total_area = min(min_total_area, area_bottom + area_top_left + area_top_right)
        
        return min_total_area

    transposed_grid = [[grid[r][c] for r in range(m)] for c in range(n)]

    result = min(solve_for_orientation(grid), solve_for_orientation(transposed_grid))
    
    return int(result)

print(xyz(g))