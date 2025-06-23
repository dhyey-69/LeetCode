# 2081. Sum of k-Mirror Numbers
# Hard
# Topics
# premium lock icon
# Companies
# Hint
# A k-mirror number is a positive integer without leading zeros that reads the same both forward and backward in base-10 as well as in base-k.

# For example, 9 is a 2-mirror number. The representation of 9 in base-10 and base-2 are 9 and 1001 respectively, which read the same both forward and backward.
# On the contrary, 4 is not a 2-mirror number. The representation of 4 in base-2 is 100, which does not read the same both forward and backward.
# Given the base k and the number n, return the sum of the n smallest k-mirror numbers.

 

# Example 1:

# Input: k = 2, n = 5
# Output: 25
# Explanation:
# The 5 smallest 2-mirror numbers and their representations in base-2 are listed as follows:
#   base-10    base-2
#     1          1
#     3          11
#     5          101
#     7          111
#     9          1001
# Their sum = 1 + 3 + 5 + 7 + 9 = 25. 
# Example 2:

# Input: k = 3, n = 7
# Output: 499
# Explanation:
# The 7 smallest 3-mirror numbers are and their representations in base-3 are listed as follows:
#   base-10    base-3
#     1          1
#     2          2
#     4          11
#     8          22
#     121        11111
#     151        12121
#     212        21212
# Their sum = 1 + 2 + 4 + 8 + 121 + 151 + 212 = 499.
# Example 3:

# Input: k = 7, n = 17
# Output: 20379000
# Explanation: The 17 smallest 7-mirror numbers are:
# 1, 2, 3, 4, 5, 6, 8, 121, 171, 242, 292, 16561, 65656, 2137312, 4602064, 6597956, 6958596
 

# Constraints:

# 2 <= k <= 9
# 1 <= n <= 30


k = 2
n = 5

# k = 3
# n = 7

# k = 7
# n = 17

def xyz(k,n):
    def to_base(num: int, base: int) -> str:
        if num == 0:
            return "0"
        digits = []
        while num:
            digits.append(str(num % base))
            num //= base
        return "".join(reversed(digits))

    def is_pal(s: str) -> bool:
        return s == s[::-1]

    found, total = 0, 0
    length = 1  

    while found < n:
        half_len = (length + 1) // 2
        start = 10 ** (half_len - 1) if length > 1 else 1
        end = 10 ** half_len

        for half in range(start, end):
            half_str = str(half)
            if length & 1:
                pal_str = half_str + half_str[-2::-1]
            else:
                pal_str = half_str + half_str[::-1]

            val = int(pal_str)
            if is_pal(to_base(val, k)):
                total += val
                found += 1
                if found == n:
                    return total
        length += 1

print(xyz(k,n))