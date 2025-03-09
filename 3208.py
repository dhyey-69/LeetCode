
# Code
# Testcase
# Test Result
# Test Result
# 3208. Alternating Groups II
# Medium
# Topics
# Companies
# Hint
# There is a circle of red and blue tiles. You are given an array of integers colors and an integer k. The color of tile i is represented by colors[i]:

# colors[i] == 0 means that tile i is red.
# colors[i] == 1 means that tile i is blue.
# An alternating group is every k contiguous tiles in the circle with alternating colors (each tile in the group except the first and last one has a different color from its left and right tiles).

# Return the number of alternating groups.

# Note that since colors represents a circle, the first and the last tiles are considered to be next to each other.

 

# Example 1:

# Input: colors = [0,1,0,1,0], k = 3

# Output: 3

# Explanation:



# Alternating groups:



# Example 2:

# Input: colors = [0,1,0,0,1,0,1], k = 6

# Output: 2

# Explanation:



# Alternating groups:



# Example 3:

# Input: colors = [1,1,0,1], k = 4

# Output: 0

# Explanation:



 

# Constraints:

# 3 <= colors.length <= 105
# 0 <= colors[i] <= 1
# 3 <= k <= colors.length

# c = [0,1,0,1,0]
# k = 3

# c = [0,1,0,0,1,0,1]
# k = 6

c = [1,1,0,1]
k = 4

def xyz(colors,k):
    # My Soultion didn't work out
    n = len(colors)
    count = 0

    for i in range(n):
        group = [colors[(i+j) % n] for j in range(k)]
        
        check = True

        for j in range(k-1):
            if group[j] == group[j+1]:
                check = False

        if check:
            count += 1

    
    return count

    # Someone else Solution
    # n = len(colors)
    # count = 0
    # left = 0

    # for right in range(n + k - 1):
    #     if right > 0 and colors[right % n] == colors[(right - 1) % n]:
    #         left = right  
            
    #     if right - left + 1 >= k:
    #         count += 1  
        
    # return count
    

print(xyz(c,k))