# 796. Rotate String

# Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

# A shift on s consists of moving the leftmost character of s to the rightmost position.

# For example, if s = "abcde", then it will be "bcdea" after one shift.
 

# Example 1:

# Input: s = "abcde", goal = "cdeab"
# Output: true
# Example 2:

# Input: s = "abcde", goal = "abced"
# Output: false
 

# Constraints:

# 1 <= s.length, goal.length <= 100
# s and goal consist of lowercase English letters.

# s1 = "abcde"
# g1 = "cdeab"

s1 = "abcde"
g1 = "abced"

def xyz(s,goal):
    temp_s = s + s

    if len(s) == len(goal):
        if goal in temp_s:
            return True
    
    return False

print(xyz(s1,g1))