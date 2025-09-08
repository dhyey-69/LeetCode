# 1317. Convert Integer to the Sum of Two No-Zero Integers
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# No-Zero integer is a positive integer that does not contain any 0 in its decimal representation.

# Given an integer n, return a list of two integers [a, b] where:

# a and b are No-Zero integers.
# a + b = n
# The test cases are generated so that there is at least one valid solution. If there are many valid solutions, you can return any of them.

 

# Example 1:

# Input: n = 2
# Output: [1,1]
# Explanation: Let a = 1 and b = 1.
# Both a and b are no-zero integers, and a + b = 2 = n.
# Example 2:

# Input: n = 11
# Output: [2,9]
# Explanation: Let a = 2 and b = 9.
# Both a and b are no-zero integers, and a + b = 11 = n.
# Note that there are other valid answers as [8, 3] that can be accepted.
 

# Constraints:

# 2 <= n <= 104


n = 2
# n = 11

def xyz(n):
    def hasZero(x):
        return '0' in str(x)
    
    for a in range(1, n):  
        b = n - a
        if not hasZero(a) and not hasZero(b):
            return [a, b]

print(xyz(n))