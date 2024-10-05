# 567. Permutation in String

# Given two strings s1 and s2, return true if s2 contains a 
# permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

 

# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
 

# Constraints:

# 1 <= s1.length, s2.length <= 104
# s1 and s2 consist of lowercase English letters.

str1 = "ab"
str2 = "eidbaooo"

def xyz(s1,s2):
    len_s1 = len(s1)
    len_s2 = len(s2)
        
    if len_s1 > len_s2:
        return False
        
    s1_count = [0] * 26
    s2_count = [0] * 26
        
    # ord(char) : it is used to generate a interger value correspodning to character like 'a' = 97 etc
    
    for char in s1:
        s1_count[ord(char) - ord('a')] += 1
        
    for i in range(len_s1):
        s2_count[ord(s2[i]) - ord('a')] += 1
        
    if s1_count == s2_count:
        return True
        
    for i in range(len_s1, len_s2):
        s2_count[ord(s2[i]) - ord('a')] += 1
        s2_count[ord(s2[i - len_s1]) - ord('a')] -= 1
        
        # print("Char",s2[i])
        # print("S1:",s1_count)
        # print("S2:",s2_count)
            
        if s1_count == s2_count:
            return True
        
    return False

xyz(str1,str2)