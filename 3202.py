# 3202. Find the Maximum Length of Valid Subsequence II
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are given an integer array nums and a positive integer k.
# A subsequence sub of nums with length x is called valid if it satisfies:

# (sub[0] + sub[1]) % k == (sub[1] + sub[2]) % k == ... == (sub[x - 2] + sub[x - 1]) % k.
# Return the length of the longest valid subsequence of nums.
 

# Example 1:

# Input: nums = [1,2,3,4,5], k = 2

# Output: 5

# Explanation:

# The longest valid subsequence is [1, 2, 3, 4, 5].

# Example 2:

# Input: nums = [1,4,2,3,1,4], k = 3

# Output: 4

# Explanation:

# The longest valid subsequence is [1, 4, 1, 4].

 

# Constraints:

# 2 <= nums.length <= 103
# 1 <= nums[i] <= 107
# 1 <= k <= 103


n = [1,2,3,4,5]
k = 2

# n = [1,4,2,3,1,4]
# k = 3

def xyz(nums,k):
    pos = [[] for _ in range(k)]
    for i, x in enumerate(nums):
        pos[x % k].append(i)
    
    residues = [r for r in range(k) if pos[r]]
    if not residues:
        return 0
    
    ans = 0
    for r in residues:
        if len(pos[r]) > ans:
            ans = len(pos[r])
    
    def alt_len(L1, L2, start_with_first):
        i = j = 0
        last = -1
        take_first = start_with_first
        picked = 0
        while True:
            if take_first:
                while i < len(L1) and L1[i] <= last:
                    i += 1
                if i == len(L1):
                    break
                last = L1[i]
                i += 1
                picked += 1
            else:
                while j < len(L2) and L2[j] <= last:
                    j += 1
                if j == len(L2):
                    break
                last = L2[j]
                j += 1
                picked += 1
            take_first = not take_first
        return picked
    
    m = len(residues)
    for a in range(m):
        La = pos[residues[a]]
        for b in range(a + 1, m):
            Lb = pos[residues[b]]
            
            if len(La) + len(Lb) <= ans:
                continue
            
            cand = alt_len(La, Lb, True)
            if cand > ans:
                ans = cand
            cand = alt_len(La, Lb, False)
            if cand > ans:
                ans = cand
    
    return ans

print(xyz(n,k))