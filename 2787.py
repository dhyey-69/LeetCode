# 2787. Ways to Express an Integer as Sum of Powers
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given two positive integers n and x.

# Return the number of ways n can be expressed as the sum of the xth power of unique positive integers, in other words, the number of sets of unique integers [n1, n2, ..., nk] where n = n1x + n2x + ... + nkx.

# Since the result can be very large, return it modulo 109 + 7.

# For example, if n = 160 and x = 3, one way to express n is n = 23 + 33 + 53.

 

# Example 1:

# Input: n = 10, x = 2
# Output: 1
# Explanation: We can express n as the following: n = 32 + 12 = 10.
# It can be shown that it is the only way to express 10 as the sum of the 2nd power of unique integers.
# Example 2:

# Input: n = 4, x = 1
# Output: 2
# Explanation: We can express n in the following ways:
# - n = 41 = 4.
# - n = 31 + 11 = 4.
 

# Constraints:

# 1 <= n <= 300
# 1 <= x <= 5

n = 10
x = 2

# n = 4
# x = 1

def xyz(n,x):
    MOD = 10**9 + 7
    
    powers = []
    base = 1
    while base ** x <= n:
        powers.append(base ** x)
        base += 1
    
    m = len(powers)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = 1
    
    for i in range(1, m + 1):
        for t in range(1, n + 1):
            dp[i][t] = dp[i - 1][t]
            if t >= powers[i - 1]:
                dp[i][t] = (dp[i][t] + dp[i - 1][t - powers[i - 1]]) % MOD
    
    return dp[m][n]

print(xyz(n,x))