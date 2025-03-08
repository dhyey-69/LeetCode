# 2379. Minimum Recolors to Get K Consecutive Black Blocks
# Easy
# Topics
# Companies
# Hint
# You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.

# You are also given an integer k, which is the desired number of consecutive black blocks.

# In one operation, you can recolor a white block such that it becomes a black block.

# Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.

 

# Example 1:

# Input: blocks = "WBBWWBBWBW", k = 7
# Output: 3
# Explanation:
# One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and 4th blocks
# so that blocks = "BBBBBBBWBW". 
# It can be shown that there is no way to achieve 7 consecutive black blocks in less than 3 operations.
# Therefore, we return 3.
# Example 2:

# Input: blocks = "WBWBBBW", k = 2
# Output: 0
# Explanation:
# No changes need to be made, since 2 consecutive black blocks already exist.
# Therefore, we return 0.
 

# Constraints:

# n == blocks.length
# 1 <= n <= 100
# blocks[i] is either 'W' or 'B'.
# 1 <= k <= n

b = "WBBWWBBWBW"
k = 7

# b = "WBWBBBW"
# k = 2

def xyz(blocks,k):
    substring = []
    strr = ""
    for i in range(len(blocks)):
        strr = ""
        for j in range(i,len(blocks)):
            strr += blocks[j]
            substring.append(strr)
    
    if 'B'*k in substring:
        return 0
    else:
        res = []
        for i in substring:
            if len(i) == 7:
                res.append(i.count('W'))
    

    return min(res)

    # Optimal Solution Using Sliding Window

    # min_ops = blocks[:k].count('W')
    # current_ops = min_ops
    
    # for i in range(1, len(blocks) - k + 1):
    #     if blocks[i - 1] == 'W':  
    #         current_ops -= 1
    #     if blocks[i + k - 1] == 'W':  
    #         current_ops += 1
        
    #     min_ops = min(min_ops, current_ops)
    
    # return min_ops

print(xyz(b,k))