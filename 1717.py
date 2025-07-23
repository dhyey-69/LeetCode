# 1717. Maximum Score From Removing Substrings
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are given a string s and two integers x and y. You can perform two types of operations any number of times.

# Remove substring "ab" and gain x points.
# For example, when removing "ab" from "cabxbae" it becomes "cxbae".
# Remove substring "ba" and gain y points.
# For example, when removing "ba" from "cabxbae" it becomes "cabxe".
# Return the maximum points you can gain after applying the above operations on s.

 

# Example 1:

# Input: s = "cdbcbbaaabab", x = 4, y = 5
# Output: 19
# Explanation:
# - Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
# - Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
# - Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
# - Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
# Total score = 5 + 4 + 5 + 5 = 19.
# Example 2:

# Input: s = "aabbaaxybbaabb", x = 5, y = 4
# Output: 20
 

# Constraints:

# 1 <= s.length <= 105
# 1 <= x, y <= 104
# s consists of lowercase English letters.

s = "cdbcbbaaabab"
x = 4
y = 5

# s = "aabbaaxybbaabb"
# x = 5
# y = 4

def xyz(s,x,y):
    def remove_substring(s, first, points):
        stack = []
        score = 0
        for char in s:
            if stack and stack[-1] == first[0] and char == first[1]:
                stack.pop()
                score += points
            else:
                stack.append(char)
        return "".join(stack), score
    
    total_score = 0
    if x >= y:
        s, score = remove_substring(s, "ab", x)
        total_score += score
        _, score = remove_substring(s, "ba", y)
        total_score += score
    else:
        s, score = remove_substring(s, "ba", y)
        total_score += score
        _, score = remove_substring(s, "ab", x)
        total_score += score
    
    return total_score

print(xyz(s,x,y))