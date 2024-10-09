# 921. Minimum Add to Make Parentheses Valid

# A parentheses string is valid if and only if:

# It is the empty string,
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
# You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

# For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
# Return the minimum number of moves required to make s valid.

 

# Example 1:

# Input: s = "())"
# Output: 1
# Example 2:

# Input: s = "((("
# Output: 3
 

# Constraints:

# 1 <= s.length <= 1000
# s[i] is either '(' or ')'.

# s1 = "())"
s1 = "((("
# s1 = "()))(("

def xyz(s):
    need_open = 0
    need_close = 0
    
    for i in s:
        if i == '(':
            need_open += 1
        elif i == ')':
            if need_open > 0:
                need_open -= 1
            else:
                need_close += 1
    
    return need_open + need_close

print(xyz(s1))