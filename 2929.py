# 2929. Distribute Candies Among Children II
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are given two positive integers n and limit.

# Return the total number of ways to distribute n candies among 3 children such that no child gets more than limit candies.

 

# Example 1:

# Input: n = 5, limit = 2
# Output: 3
# Explanation: There are 3 ways to distribute 5 candies such that no child gets more than 2 candies: (1, 2, 2), (2, 1, 2) and (2, 2, 1).
# Example 2:

# Input: n = 3, limit = 3
# Output: 10
# Explanation: There are 10 ways to distribute 3 candies such that no child gets more than 3 candies: (0, 0, 3), (0, 1, 2), (0, 2, 1), (0, 3, 0), (1, 0, 2), (1, 1, 1), (1, 2, 0), (2, 0, 1), (2, 1, 0) and (3, 0, 0).
 

# Constraints:

# 1 <= n <= 106
# 1 <= limit <= 106

n = 5
l = 2

# n = 3
# l = 3

def xyz(n,limit):
    def comb(n, r):
        if r > n or r < 0:
            return 0
        if r > n - r:
            r = n - r
        res = 1
        for i in range(r):
            res = res * (n - i) // (i + 1)
        return res
        
    total = comb(n + 2, 2)
    
    subtract = 3 * comb(n - (limit + 1) + 2, 2) if n - (limit + 1) >= 0 else 0
    
    add_back = 3 * comb(n - 2 * (limit + 1) + 2, 2) if n - 2 * (limit + 1) >= 0 else 0
    
    subtract_three = comb(n - 3 * (limit + 1) + 2, 2) if n - 3 * (limit + 1) >= 0 else 0

    print("Total :",total)
    print("Subtract : ",subtract)
    print("Add Back:",add_back)
    print("Subtract Three" , subtract_three)
    
    return total - subtract + add_back - subtract_three


print(xyz(n,l))