# Code
# Testcase
# Test Result
# Test Result
# 763. Partition Labels
# Medium
# Topics
# Companies
# Hint
# You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part. For example, the string "ababcc" can be partitioned into ["abab", "cc"], but partitions such as ["aba", "bcc"] or ["ab", "ab", "cc"] are invalid.

# Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

# Return a list of integers representing the size of these parts.

 

# Example 1:

# Input: s = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
# Example 2:

# Input: s = "eccbbbbdec"
# Output: [10]
 

# Constraints:

# 1 <= s.length <= 500
# s consists of lowercase English letters.

s = "ababcbacadefegdehijhklij"
# s = "eccbbbbdec"

def xyz(s):
    last_index = {char: idx for idx, char in enumerate(s)}
        
    partitions = []
    start, end = 0, 0
        
    for i, char in enumerate(s):
        end = max(end, last_index[char])
            
        if i == end:
            partitions.append(end - start + 1)
            start = i + 1
        
    return partitions

print(xyz(s))