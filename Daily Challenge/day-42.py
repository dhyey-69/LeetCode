# 2406. Divide Intervals Into Minimum Number of Groups

# You are given a 2D integer array intervals where intervals[i] = [lefti, righti] represents the inclusive interval [lefti, righti].

# You have to divide the intervals into one or more groups such that each interval is in exactly one group, and no two intervals that are in the same group intersect each other.

# Return the minimum number of groups you need to make.

# Two intervals intersect if there is at least one common number between them. For example, the intervals [1, 5] and [5, 8] intersect.

 

# Example 1:

# Input: intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]
# Output: 3
# Explanation: We can divide the intervals into the following groups:
# - Group 1: [1, 5], [6, 8].
# - Group 2: [2, 3], [5, 10].
# - Group 3: [1, 10].
# It can be proven that it is not possible to divide the intervals into fewer than 3 groups.
# Example 2:

# Input: intervals = [[1,3],[5,6],[8,10],[11,13]]
# Output: 1
# Explanation: None of the intervals overlap, so we can put all of them in one group.
 

# Constraints:

# 1 <= intervals.length <= 105
# intervals[i].length == 2
# 1 <= lefti <= righti <= 106

intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]

def xyz(intervals):
    events = []
        
    # For each interval, we add two events:
    # 1. +1 at the start of the interval
    # 2. -1 at the end of the interval + 1
    for start, end in intervals:
        events.append((start, 1))   # Interval starts
        events.append((end + 1, -1))  # Interval ends

    # Sort the events by time
    events.sort()

    # Track the current number of overlapping intervals
    current_overlap = 0
    max_overlap = 0
        
    # Sweep through all the events
    for event in events:
        current_overlap += event[1]
        max_overlap = max(max_overlap, current_overlap)
        
    return max_overlap

print(xyz(intervals))