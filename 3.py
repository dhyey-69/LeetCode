# Given a string s, find the length of the longest substring without repeating characters.
# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

s = "abcabcbb"

def xyz(str):
    char_index = {}
    max_len = 0
    start = 0
        
    for i, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        
        char_index[char] = i
           
        max_len = max(max_len, i - start + 1)
    
    return max_len

print(xyz(s))