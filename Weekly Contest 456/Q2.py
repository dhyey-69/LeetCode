# Q2. Longest Common Prefix Between Adjacent Strings After Removals
# Attempted
# Medium
# 4 pt.
# You are given an array of strings words. For each index i in the range [0, words.length - 1], perform the following steps:

# Remove the element at index i from the words array.
# Compute the length of the longest common prefix among all adjacent pairs in the modified array.
# Return an array answer, where answer[i] is the length of the longest common prefix between the adjacent pairs after removing the element at index i. If no adjacent pairs remain or if none share a common prefix, then answer[i] should be 0.

# A prefix of a string is a substring that starts from the beginning of the string and extends to any point within it.
 

# Example 1:

# Input: words = ["jump","run","run","jump","run"]

# Output: [3,0,0,3,3]

# Explanation:

# Removing index 0:
# words becomes ["run", "run", "jump", "run"]
# Longest adjacent pair is ["run", "run"] having a common prefix "run" (length 3)
# Removing index 1:
# words becomes ["jump", "run", "jump", "run"]
# No adjacent pairs share a common prefix (length 0)
# Removing index 2:
# words becomes ["jump", "run", "jump", "run"]
# No adjacent pairs share a common prefix (length 0)
# Removing index 3:
# words becomes ["jump", "run", "run", "run"]
# Longest adjacent pair is ["run", "run"] having a common prefix "run" (length 3)
# Removing index 4:
# words becomes ["jump", "run", "run", "jump"]
# Longest adjacent pair is ["run", "run"] having a common prefix "run" (length 3)
# Example 2:

# Input: words = ["dog","racer","car"]

# Output: [0,0,0]

# Explanation:

# Removing any index results in an answer of 0.
 

# Constraints:

# 1 <= words.length <= 105
# 1 <= words[i].length <= 104
# words[i] consists of lowercase English letters.
# The sum of words[i].length is smaller than or equal 105.


w = ["jump","run","run","jump","run"]
# w = ["dog","racer","car"]


def xyz(words):
    def common_prefix_len(a: str, b: str) -> int:
        i = 0
        while i < min(len(a), len(b)) and a[i] == b[i]:
            i += 1
        return i
    
    n = len(words)
    if n == 1:
        return [0]
    
    prefix_lens = [common_prefix_len(words[i], words[i + 1]) for i in range(n - 1)]
    global_max = max(prefix_lens)

    result = []
    for i in range(n):
        if n == 2:
            result.append(0)
            continue

        if i == 0:
            result.append(max(prefix_lens[1:]) if len(prefix_lens) > 1 else 0)
        elif i == n - 1:
            result.append(max(prefix_lens[:-1]) if len(prefix_lens) > 1 else 0)
        else:
            left = prefix_lens[i - 1]
            right = prefix_lens[i]
            new_lcp = common_prefix_len(words[i - 1], words[i + 1])

            if global_max == left or global_max == right:
                remaining = prefix_lens[:i - 1] + prefix_lens[i + 1:]
                remaining_max = max(remaining) if remaining else 0
            else:
                remaining_max = global_max

            result.append(max(new_lcp, remaining_max))

    return result


print(xyz(w))