# 214. Shortest Palindrome
# Hard
# You are given a string s. You can convert s to a 
# palindrome
#  by adding characters in front of it.

# Return the shortest palindrome you can find by performing this transformation.

 

# Example 1:

# Input: s = "aacecaaa"
# Output: "aaacecaaa"
# Example 2:

# Input: s = "abcd"
# Output: "dcbabcd"

# Example 3:

# Input: s = "abbacd"
# Output: "dcabbacd"


s1 = "abbacd"

def xyz(s):
    # if (s == s[::-1]):
    #     return s
    
    # temp = s    
    
    # for i in range(len(s)+1):
    #     if s[i] != s[i+1]:
    #         temp = s[:i:-1] + temp
    #         return temp
    #     temp = s[i] + temp
    #     print(temp)
    #     if temp == temp[::-1]:
    #         return temp

# s1 = "abbacd"
    if s == s[::-1]:
        return s

    rev_s = s[::-1]
    
    for i in range(len(s)):
        # print(rev_s[i:])
        if s.startswith(rev_s[i:]):
            return rev_s[:i] + s
        
    return ""

print(xyz(s1))