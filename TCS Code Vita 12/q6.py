from collections import defaultdict
import math

def on_segment(p, q, r):
    """ Returns True if point q lies on the line segment pr """
    if min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and min(p[1], r[1]) <= q[1] <= max(p[1], r[1]):
        return True
    return False

def orientation(p, q, r):
    """ Find the orientation of the triplet (p, q, r).
        0 -> p, q and r are collinear
        1 -> Clockwise
        2 -> Counterclockwise
    """
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2

def do_intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    """ Returns True if line segment (x1, y1) to (x2, y2) and (x3, y3) to (x4, y4) intersect """
    o1 = orientation((x1, y1), (x2, y2), (x3, y3))
    o2 = orientation((x1, y1), (x2, y2), (x4, y4))
    o3 = orientation((x3, y3), (x4, y4), (x1, y1))
    o4 = orientation((x3, y3), (x4, y4), (x2, y2))
    
    # General case
    if o1 != o2 and o3 != o4:
        return True
    
    # Special cases
    # p1, q1, p2 are collinear and p2 lies on segment p1q1
    if o1 == 0 and on_segment((x1, y1), (x3, y3), (x2, y2)):
        return True
    
    # p1, q1, p2 are collinear and q2 lies on segment p1q1
    if o2 == 0 and on_segment((x1, y1), (x4, y4), (x2, y2)):
        return True
    
    # p2, q2, p1 are collinear and p1 lies on segment p2q2
    if o3 == 0 and on_segment((x3, y3), (x1, y1), (x4, y4)):
        return True
    
    # p2, q2, q1 are collinear and q1 lies on segment p2q2
    if o4 == 0 and on_segment((x3, y3), (x2, y2), (x4, y4)):
        return True
    
    return False

def get_intensity_of_star(lines, intersection):
    """ Calculate intensity of star formed at a given intersection point """
    intensities = []
    
    for line in lines:
        x1, y1, x2, y2 = line
        
        if x1 == x2:  # Vertical line
            if x1 == intersection[0]:
                # Count cells vertically from intersection
                up = intersection[1] - y1
                down = y2 - intersection[1]
                intensities.append(min(abs(up), abs(down)))
        elif y1 == y2:  # Horizontal line
            if y1 == intersection[1]:
                # Count cells horizontally from intersection
                left = intersection[0] - x1
                right = x2 - intersection[0]
                intensities.append(min(abs(left), abs(right)))
        else:
            # Diagonal line, use geometric reasoning to count cells.
            pass
    
    return min(intensities)

def main():
    N = int(input())  # Number of lines
    lines = []
    for _ in range(N):
        x1, y1, x2, y2 = map(int, input().split())
        lines.append((x1, y1, x2, y2))
    
    K = int(input())  # Type of star (2 to 8)
    
    intersection_points = defaultdict(int)
    
    # Identify all intersection points
    for i in range(N):
        for j in range(i+1, N):
            line1 = lines[i]
            line2 = lines[j]
            
            # Unpack the lines to individual points
            x1, y1, x2, y2 = line1
            x3, y3, x4, y4 = line2
            
            # Check if the lines intersect
            if do_intersect(x1, y1, x2, y2, x3, y3, x4, y4):
                # Compute intersection point of lines i and j (this step requires geometry)
                # For simplicity, you need to add the logic to find the exact intersection point.
                pass
    
    total_intensity = 0
    for point, count in intersection_points.items():
        if count == K:
            intensity = get_intensity_of_star(lines, point)
            total_intensity += intensity
    
    print(total_intensity)

# Calling the main function to execute the program
if __name__ == "__main__":
    main()
