# 3003. Maximize the Number of Partitions After Operations
# Hard
# Topics
# premium lock icon
# Companies
# Hint
# You are given a string s and an integer k.

# First, you are allowed to change at most one index in s to another lowercase English letter.

# After that, do the following partitioning operation until s is empty:

# Choose the longest prefix of s containing at most k distinct characters.
# Delete the prefix from s and increase the number of partitions by one. The remaining characters (if any) in s maintain their initial order.
# Return an integer denoting the maximum number of resulting partitions after the operations by optimally choosing at most one index to change.

 

# Example 1:

# Input: s = "accca", k = 2

# Output: 3

# Explanation:

# The optimal way is to change s[2] to something other than a and c, for example, b. then it becomes "acbca".

# Then we perform the operations:

# The longest prefix containing at most 2 distinct characters is "ac", we remove it and s becomes "bca".
# Now The longest prefix containing at most 2 distinct characters is "bc", so we remove it and s becomes "a".
# Finally, we remove "a" and s becomes empty, so the procedure ends.
# Doing the operations, the string is divided into 3 partitions, so the answer is 3.

# Example 2:

# Input: s = "aabaab", k = 3

# Output: 1

# Explanation:

# Initially s contains 2 distinct characters, so whichever character we change, it will contain at most 3 distinct characters, so the longest prefix with at most 3 distinct characters would always be all of it, therefore the answer is 1.

# Example 3:

# Input: s = "xxyz", k = 1

# Output: 4

# Explanation:

# The optimal way is to change s[0] or s[1] to something other than characters in s, for example, to change s[0] to w.

# Then s becomes "wxyz", which consists of 4 distinct characters, so as k is 1, it will divide into 4 partitions.

 

# Constraints:

# 1 <= s.length <= 104
# s consists only of lowercase English letters.
# 1 <= k <= 26


s = "accca"
k = 2

# s = "aabaab"
# k = 3

# s = "xxyz"
# k = 1

ALPHABET_SIZE = 26

def xyz(s,k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    if k == ALPHABET_SIZE:
        return 1

    n = len(s)
    ansr = [0] * n
    usedr = [0] * n
    used = 0
    cntUsed = 0
    ans = 1

    for i in range(n - 1, -1, -1):
        ch = ord(s[i]) - ord('a')
        if (used & (1 << ch)) == 0:
            if cntUsed == k:
                cntUsed = 0
                used = 0
                ans += 1
            used |= (1 << ch)
            cntUsed += 1
        ansr[i] = ans
        usedr[i] = used

    ansl = 0
    ans = ansr[0]

    l = 0
    while l < n:
        used = 0
        cntUsed = 0
        usedBeforeLast = 0
        usedTwiceBeforeLast = 0
        last = -1
        r = l

        while r < n:
            ch = ord(s[r]) - ord('a')
            if (used & (1 << ch)) == 0:
                if cntUsed == k:
                    break
                usedBeforeLast = used
                last = r
                used |= (1 << ch)
                cntUsed += 1
            elif cntUsed < k:
                usedTwiceBeforeLast |= (1 << ch)
            r += 1

        if cntUsed == k:
            if last - l > bin(usedBeforeLast).count('1'):
                ans = max(ans, ansl + 1 + ansr[last])
            if last + 1 < r:
                if last + 2 >= n:
                    ans = max(ans, ansl + 1 + 1)
                else:
                    if bin(usedr[last + 2]).count('1') == k:
                        canUse = ((1 << ALPHABET_SIZE) - 1) & ~used & ~usedr[last + 2]
                        if canUse > 0:
                            ans = max(ans, ansl + 1 + 1 + ansr[last + 2])
                        else:
                            ans = max(ans, ansl + 1 + ansr[last + 2])
                        l1 = ord(s[last + 1]) - ord('a')
                        if (usedTwiceBeforeLast & (1 << l1)) == 0:
                            ans = max(ans, ansl + 1 + ansr[last + 1])
                    else:
                        ans = max(ans, ansl + 1 + ansr[last + 2])

        l = r
        ansl += 1

    return ans

print(xyz(s,k))