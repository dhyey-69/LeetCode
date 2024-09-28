# 884. Uncommon Words from Two Sentences

# A sentence is a string of single-space separated words where each word consists only of lowercase letters.

# A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

# Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

 

# Example 1:

# Input: s1 = "this apple is sweet", s2 = "this apple is sour"

# Output: ["sweet","sour"]

# Explanation:

# The word "sweet" appears only in s1, while the word "sour" appears only in s2.

# Example 2:

# Input: s1 = "apple apple", s2 = "banana"

# Output: ["banana"]

str1 = "apple apple"
str2 =  "banana"

def xyz(s1,s2):
    l1 = s1.split(" ")
    l2 = s2.split(" ")
    
    result = []
    for i in l1:
        if (i not in l2) and (l1.count(i) == 1):
            result.append(i)

    for i in l2:
        if i not in l1 and (l2.count(i) == 1):
            result.append(i)

    return result

print(xyz(str1,str2))