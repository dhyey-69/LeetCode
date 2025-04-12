# 3272. Find the Count of Good Integers
# Hard
# Topics
# Companies
# Hint
# You are given two positive integers n and k.

# An integer x is called k-palindromic if:

# x is a palindrome.
# x is divisible by k.
# An integer is called good if its digits can be rearranged to form a k-palindromic integer. For example, for k = 2, 2020 can be rearranged to form the k-palindromic integer 2002, whereas 1010 cannot be rearranged to form a k-palindromic integer.

# Return the count of good integers containing n digits.

# Note that any integer must not have leading zeros, neither before nor after rearrangement. For example, 1010 cannot be rearranged to form 101.

 

# Example 1:

# Input: n = 3, k = 5

# Output: 27

# Explanation:

# Some of the good integers are:

# 551 because it can be rearranged to form 515.
# 525 because it is already k-palindromic.
# Example 2:

# Input: n = 1, k = 4

# Output: 2

# Explanation:

# The two good integers are 4 and 8.

# Example 3:

# Input: n = 5, k = 6

# Output: 2468

 

# Constraints:

# 1 <= n <= 10
# 1 <= k <= 9

n = 3
k = 5

# n = 1
# k = 4

# n = 5
# k = 6

def xyz(n,k):
        def factorial(x):
            res = 1
            for i in range(2, x + 1):
                res *= i
            return res

        def count_permutations(freq):
            total = sum(freq)
            res = factorial(total)
            for f in freq:
                res //= factorial(f)
            return res

        def count_valid_permutations(freq):
            total = 0
            for d in range(1, 10):
                if freq[d] == 0:
                    continue
                freq[d] -= 1
                total += count_permutations(freq)
                freq[d] += 1
            return total

        def generate_palindromes(n):
            half = (n + 1) // 2
            start = 10 ** (half - 1)
            end = 10 ** half
            for num in range(start, end):
                s = str(num)
                if n % 2 == 0:
                    pal = s + s[::-1]
                else:
                    pal = s + s[-2::-1]
                yield int(pal)

        seen = set()
        result = 0
        for pal in generate_palindromes(n):
            if pal % k != 0:
                continue
            freq = [0] * 10
            for ch in str(pal):
                freq[int(ch)] += 1
            key = tuple(freq)
            if key in seen:
                continue
            seen.add(key)
            result += count_valid_permutations(freq)
        return result

print(xyz(n,k))