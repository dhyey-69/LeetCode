# 2528. Maximize the Minimum Powered City
# Hard
# Topics
# premium lock icon
# Companies
# Hint
# You are given a 0-indexed integer array stations of length n, where stations[i] represents the number of power stations in the ith city.

# Each power station can provide power to every city in a fixed range. In other words, if the range is denoted by r, then a power station at city i can provide power to all cities j such that |i - j| <= r and 0 <= i, j <= n - 1.

# Note that |x| denotes absolute value. For example, |7 - 5| = 2 and |3 - 10| = 7.
# The power of a city is the total number of power stations it is being provided power from.

# The government has sanctioned building k more power stations, each of which can be built in any city, and have the same range as the pre-existing ones.

# Given the two integers r and k, return the maximum possible minimum power of a city, if the additional power stations are built optimally.

# Note that you can build the k power stations in multiple cities.

 

# Example 1:

# Input: stations = [1,2,4,5,0], r = 1, k = 2
# Output: 5
# Explanation: 
# One of the optimal ways is to install both the power stations at city 1. 
# So stations will become [1,4,4,5,0].
# - City 0 is provided by 1 + 4 = 5 power stations.
# - City 1 is provided by 1 + 4 + 4 = 9 power stations.
# - City 2 is provided by 4 + 4 + 5 = 13 power stations.
# - City 3 is provided by 5 + 4 = 9 power stations.
# - City 4 is provided by 5 + 0 = 5 power stations.
# So the minimum power of a city is 5.
# Since it is not possible to obtain a larger power, we return 5.
# Example 2:

# Input: stations = [4,4,4,4], r = 0, k = 3
# Output: 4
# Explanation: 
# It can be proved that we cannot make the minimum power of a city greater than 4.
 

# Constraints:

# n == stations.length
# 1 <= n <= 105
# 0 <= stations[i] <= 105
# 0 <= r <= n - 1
# 0 <= k <= 109


s = [1,2,4,5,0]
r = 1
k = 2

# s = [4,4,4,4]
# r = 0
# k = 3

def xyz(stations,r,k):
    n = len(stations)
    pref = [0] * (n + 1)
    for i in range(n):
        pref[i + 1] = pref[i] + stations[i]
    power = [0] * n
    for i in range(n):
        L = max(0, i - r)
        R = min(n - 1, i + r)
        power[i] = pref[R + 1] - pref[L]
    
    def can(x):
        adds = [0] * n
        addedWindow = 0
        used = 0
        for i in range(n):
            out_idx = i - r - 1
            if out_idx >= 0:
                addedWindow -= adds[out_idx]
            total = power[i] + addedWindow
            if total < x:
                need = x - total
                used += need
                if used > k:
                    return False
                pos = min(n - 1, i + r)
                adds[pos] += need
                addedWindow += need
        return True
    
    lo, hi = 0, sum(stations) + k
    ans = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if can(mid):
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return ans

print(xyz(s,r,k))