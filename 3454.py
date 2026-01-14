# 3454. Separate Squares II
# Hard
# Topics
# premium lock icon
# Companies
# Hint
# You are given a 2D integer array squares. Each squares[i] = [xi, yi, li] represents the coordinates of the bottom-left point and the side length of a square parallel to the x-axis.

# Find the minimum y-coordinate value of a horizontal line such that the total area covered by squares above the line equals the total area covered by squares below the line.

# Answers within 10-5 of the actual answer will be accepted.

# Note: Squares may overlap. Overlapping areas should be counted only once in this version.

 

# Example 1:

# Input: squares = [[0,0,1],[2,2,1]]

# Output: 1.00000

# Explanation:



# Any horizontal line between y = 1 and y = 2 results in an equal split, with 1 square unit above and 1 square unit below. The minimum y-value is 1.

# Example 2:

# Input: squares = [[0,0,2],[1,1,1]]

# Output: 1.00000

# Explanation:



# Since the blue square overlaps with the red square, it will not be counted again. Thus, the line y = 1 splits the squares into two equal parts.

 

# Constraints:

# 1 <= squares.length <= 5 * 104
# squares[i] = [xi, yi, li]
# squares[i].length == 3
# 0 <= xi, yi <= 109
# 1 <= li <= 109
# The total area of all the squares will not exceed 1015.



s = [[0,0,1],[2,2,1]]
# s = [[0,0,2],[1,1,1]]

def xyz(squares):
    events = []
    xs = {}

    for x, y, l in squares:
        x1 = x
        x2 = x + l
        y1 = y
        y2 = y + l
        events.append([y1, 1, x1, x2])
        events.append([y2, -1, x1, x2])
        xs[x1] = 1
        xs[x2] = 1

    xs = list(xs.keys())
    xs.sort()
    x_index = {}
    for i in range(len(xs)):
        x_index[xs[i]] = i

    n = len(xs) - 1
    count = [0] * (4 * n)
    length = [0] * (4 * n)

    def push_up(node, l, r):
        if count[node] > 0:
            length[node] = xs[r] - xs[l]
        elif l + 1 == r:
            length[node] = 0
        else:
            length[node] = length[node * 2] + length[node * 2 + 1]

    def update(node, l, r, ql, qr, val):
        if qr <= l or r <= ql:
            return
        if ql <= l and r <= qr:
            count[node] += val
            push_up(node, l, r)
            return
        mid = (l + r) // 2
        update(node * 2, l, mid, ql, qr, val)
        update(node * 2 + 1, mid, r, ql, qr, val)
        push_up(node, l, r)

    events.sort(key=lambda e: e[0])

    cur_area = 0.0
    last_y = events[0][0]

    for y, typ, x1, x2 in events:
        dy = y - last_y
        if dy > 0:
            cur_area += length[1] * dy
        update(1, 0, n, x_index[x1], x_index[x2], typ)
        last_y = y

    half = cur_area / 2.0

    count = [0] * (4 * n)
    length = [0] * (4 * n)
    cur_area = 0.0
    last_y = events[0][0]

    for y, typ, x1, x2 in events:
        dy = y - last_y
        if dy > 0:
            strip_area = length[1] * dy
            if cur_area + strip_area >= half:
                if length[1] == 0:
                    return float(last_y)
                return last_y + (half - cur_area) / length[1]
            cur_area += strip_area
        update(1, 0, n, x_index[x1], x_index[x2], typ)
        last_y = y

    return float(last_y)


print(xyz(s))