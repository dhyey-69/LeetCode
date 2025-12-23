# 2054. Two Best Non-Overlapping Events
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are given a 0-indexed 2D integer array of events where events[i] = [startTimei, endTimei, valuei]. The ith event starts at startTimei and ends at endTimei, and if you attend this event, you will receive a value of valuei. You can choose at most two non-overlapping events to attend such that the sum of their values is maximized.

# Return this maximum sum.

# Note that the start time and end time is inclusive: that is, you cannot attend two events where one of them starts and the other ends at the same time. More specifically, if you attend an event with end time t, the next event must start at or after t + 1.

 

# Example 1:


# Input: events = [[1,3,2],[4,5,2],[2,4,3]]
# Output: 4
# Explanation: Choose the green events, 0 and 1 for a sum of 2 + 2 = 4.
# Example 2:

# Example 1 Diagram
# Input: events = [[1,3,2],[4,5,2],[1,5,5]]
# Output: 5
# Explanation: Choose event 2 for a sum of 5.
# Example 3:


# Input: events = [[1,5,3],[1,5,1],[6,6,5]]
# Output: 8
# Explanation: Choose events 0 and 2 for a sum of 3 + 5 = 8.
 

# Constraints:

# 2 <= events.length <= 105
# events[i].length == 3
# 1 <= startTimei <= endTimei <= 109
# 1 <= valuei <= 106


e = [[1,3,2],[4,5,2],[2,4,3]]
# e = [[1,3,2],[4,5,2],[1,5,5]]
# e = [[1,5,3],[1,5,1],[6,6,5]]

def xyz(events):
    events.sort(key=lambda x: x[1])
    n = len(events)

    ends = [events[i][1] for i in range(n)]

    best = [0] * n
    best[0] = events[0][2]
    for i in range(1, n):
        best[i] = max(best[i - 1], events[i][2])

    ans = 0

    for s, e, v in events:
        lo, hi = 0, n - 1
        idx = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if ends[mid] < s:
                idx = mid
                lo = mid + 1
            else:
                hi = mid - 1

        if idx != -1:
            ans = max(ans, v + best[idx])
        else:
            ans = max(ans, v)

    return ans

print(xyz(e))