# 1780. Check if Number is a Sum of Powers of Three
# Medium
# Topics
# Companies
# Hint
# Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three. Otherwise, return false.

# An integer y is a power of three if there exists an integer x such that y == 3x.

 

# Example 1:

# Input: n = 12
# Output: true
# Explanation: 12 = 31 + 32
# Example 2:

# Input: n = 91
# Output: true
# Explanation: 91 = 30 + 32 + 34
# Example 3:

# Input: n = 21
# Output: false
 

# Constraints:

# 1 <= n <= 107

# num = 12
num = 91
# num = 21

def xyz(n):
    # check = True

    # while (n > 0):
    #     n, rem = divmod(n, 3)
    #     if rem == 2:
    #         check = False
    # return check

    while n > 0:
        if n % 3 == 2:
            return False
        n //= 3
    
    return True
        
print(xyz(num))