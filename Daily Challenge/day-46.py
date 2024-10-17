# 1405. Longest Happy String

# A string s is called happy if it satisfies the following conditions:

# s only contains the letters 'a', 'b', and 'c'.
# s does not contain any of "aaa", "bbb", or "ccc" as a substring.
# s contains at most a occurrences of the letter 'a'.
# s contains at most b occurrences of the letter 'b'.
# s contains at most c occurrences of the letter 'c'.
# Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

# A substring is a contiguous sequence of characters within a string.

 

# Example 1:

# Input: a = 1, b = 1, c = 7
# Output: "ccaccbcc"
# Explanation: "ccbccacc" would also be a correct answer.
# Example 2:

# Input: a = 7, b = 1, c = 0
# Output: "aabaa"
# Explanation: It is the only correct answer in this case.
 

# Constraints:

# 0 <= a, b, c <= 100
# a + b + c > 0

a = 1
b = 1 
c = 7

def xyz(a,b,c):
    counts = [['a', a], ['b', b], ['c', c]]
        
    result = []

    while True:
        counts.sort(key=lambda x: -x[1])
            
        added = False
            
        for i in range(3):
            char, count = counts[i]
            if count == 0:
                continue
                
            if len(result) >= 2 and result[-1] == result[-2] == char:
                continue
                
            result.append(char)
            counts[i][1] -= 1
            added = True
            break
            
        if not added:
            break
        
    return ''.join(result)

print(xyz(a,b,c))