
# Code
# Testcase
# Test Result
# Test Result
# 3306. Count of Substrings Containing Every Vowel and K Consonants II
# Medium
# Topics
# Companies
# Hint
# You are given a string word and a non-negative integer k.

# Return the total number of substrings of word that contain every vowel ('a', 'e', 'i', 'o', and 'u') at least once and exactly k consonants.

 

# Example 1:

# Input: word = "aeioqq", k = 1

# Output: 0

# Explanation:

# There is no substring with every vowel.

# Example 2:

# Input: word = "aeiou", k = 0

# Output: 1

# Explanation:

# The only substring with every vowel and zero consonants is word[0..4], which is "aeiou".

# Example 3:

# Input: word = "ieaouqqieaouqq", k = 1

# Output: 3

# Explanation:

# The substrings with every vowel and one consonant are:

# word[0..5], which is "ieaouq".
# word[6..11], which is "qieaou".
# word[7..12], which is "ieaouq".
 

# Constraints:

# 5 <= word.length <= 2 * 105
# word consists only of lowercase English letters.
# 0 <= k <= word.length - 5

from collections import defaultdict


w = "aeioqq"
k = 1

# w = "aeiou"
# k = 0

# w = "ieaouqqieaouqq"
# k = 1

def xyz(word,k):
    # My Solution which correct but ineffecient one
    
    # if len(word) < 5:
    #     return 0
    
    # count = 0
    # substring = []
    # strr = ""
    # for i in range(len(word)):
    #     strr = ""
    #     for j in range(i,len(word)):
    #         strr += word[j]
    #         if len(strr) >= k + 5:
    #             substring.append(strr)
    
    # for i in substring:
    #     if (i.count('a') > 0) and (i.count('e') > 0) and (i.count('i') > 0) and (i.count('o') > 0) and (i.count('u') > 0):
    #         len_con = len(i) - i.count('a') - i.count('e') - i.count('i') - i.count('o') - i.count('u')
    #         if (len_con == k):
    #             print(i)
    #             count += 1
    # return count

    # Optimal Solution
    n = len(word)
    vowels = set('aeiou')
    vowel_count, cons_count = defaultdict(int), 0
    left = count = substrs = 0

    def minus_char(char):
        if char in vowels:
            vowel_count[char] -= 1
            if vowel_count[char] == 0:
                del vowel_count[char]
        else:
            nonlocal cons_count
            cons_count -= 1

    for char in word:
        if char in vowels:
            vowel_count[char] += 1
        else:
            cons_count += 1
            count = 0

        while cons_count > k:
            minus_char(word[left])
            left += 1

        while cons_count == k and len(vowel_count) == 5:
            count += 1
            minus_char(word[left])
            left += 1
            
        substrs += count

    return substrs

print(xyz(w,k))