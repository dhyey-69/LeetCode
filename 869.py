# 869. Reordered Power of 2
# Medium
# Topics
# premium lock icon
# Companies
# You are given an integer n. We reorder the digits in any order (including the original order) such that the leading digit is not zero.

# Return true if and only if we can do this so that the resulting number is a power of two.

 

# Example 1:

# Input: n = 1
# Output: true
# Example 2:

# Input: n = 10
# Output: false
 

# Constraints:

# 1 <= n <= 109

n = 1
# n = 10

def xyz(n):
    def signature(x):
        return "".join(sorted(str(x)))
    
    target_sig = signature(n)
    for i in range(31):
        if signature(1 << i) == target_sig:
            return True
    return False

print(xyz(n))