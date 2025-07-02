# 3333. Find the Original Typed String II
# Hard
# Topics
# premium lock icon
# Companies
# Hint
# Alice is attempting to type a specific string on her computer. However, she tends to be clumsy and may press a key for too long, resulting in a character being typed multiple times.

# You are given a string word, which represents the final output displayed on Alice's screen. You are also given a positive integer k.

# Return the total number of possible original strings that Alice might have intended to type, if she was trying to type a string of size at least k.

# Since the answer may be very large, return it modulo 109 + 7.

 

# Example 1:

# Input: word = "aabbccdd", k = 7

# Output: 5

# Explanation:

# The possible strings are: "aabbccdd", "aabbccd", "aabbcdd", "aabccdd", and "abbccdd".

# Example 2:

# Input: word = "aabbccdd", k = 8

# Output: 1

# Explanation:

# The only possible string is "aabbccdd".

# Example 3:

# Input: word = "aaabbb", k = 3

# Output: 8

 

# Constraints:

# 1 <= word.length <= 5 * 105
# word consists only of lowercase English letters.
# 1 <= k <= 2000


w = "aabbccdd"
k = 7

w = "aabbccdd"
k = 8

w = "aaabbb"
k = 3

MOD = 10**9 + 7

def xyz(word,k):
    if not word:
        return 0
    groups = []
    count = 1
    for i in range(1, len(word)):
        if word[i] == word[i - 1]:
            count += 1
        else:
            groups.append(count)
            count = 1
    groups.append(count)
    total = 1
    for num in groups:
        total = (total * num) % MOD

    if k <= len(groups):
        return total
    dp = [0] * k
    dp[0] = 1
    for num in groups:
        new_dp = [0] * k
        sum_val = 0
        for s in range(k):
            if s > 0:
                sum_val = (sum_val + dp[s - 1]) % MOD
            if s > num:
                sum_val = (sum_val - dp[s - num - 1] + MOD) % MOD
            new_dp[s] = sum_val
        dp = new_dp

    invalid = sum(dp[len(groups):k]) % MOD
    return (total - invalid + MOD) % MOD

print(xyz(w,k))