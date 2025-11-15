# 3234. Count the Number of Substrings With Dominant Ones
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are given a binary string s.

# Return the number of substrings with dominant ones.

# A string has dominant ones if the number of ones in the string is greater than or equal to the square of the number of zeros in the string.

 

# Example 1:

# Input: s = "00011"

# Output: 5

# Explanation:

# The substrings with dominant ones are shown in the table below.

# i	j	s[i..j]	Number of Zeros	Number of Ones
# 3	3	1	0	1
# 4	4	1	0	1
# 2	3	01	1	1
# 3	4	11	0	2
# 2	4	011	1	2
# Example 2:

# Input: s = "101101"

# Output: 16

# Explanation:

# The substrings with non-dominant ones are shown in the table below.

# Since there are 21 substrings total and 5 of them have non-dominant ones, it follows that there are 16 substrings with dominant ones.

# i	j	s[i..j]	Number of Zeros	Number of Ones
# 1	1	0	1	0
# 4	4	0	1	0
# 1	4	0110	2	2
# 0	4	10110	2	3
# 1	5	01101	2	3
 

# Constraints:

# 1 <= s.length <= 4 * 104
# s consists only of characters '0' and '1'.


s = "00011"
# s = "101101"

def xyz(s):
    n = len(s)
    pz = [0] * (n + 1)
    po = [0] * (n + 1)
    for i, ch in enumerate(s):
        pz[i + 1] = pz[i] + (ch == '0')
        po[i + 1] = po[i] + (ch == '1')

    zeros = []
    for i, ch in enumerate(s):
        if ch == '0':
            zeros.append(i)
    zlen = len(zeros)

    def first_ge(x):
        lo, hi = 0, zlen
        while lo < hi:
            mid = (lo + hi) // 2
            if zeros[mid] < x:
                lo = mid + 1
            else:
                hi = mid
        return lo

    import_limit = int(n ** 0.5) + 2
    max_k = import_limit

    total = 0

    for l in range(n):
        zi = first_ge(l)

        for k in range(max_k + 1):
            if zi + k > zlen:
                break

            if k == 0:
                if zi < zlen:
                    r0 = l
                    r1 = zeros[zi] - 1
                else:
                    r0 = l
                    r1 = n - 1
            else:
                r0 = zeros[zi + k - 1]
                if zi + k < zlen:
                    r1 = zeros[zi + k] - 1
                else:
                    r1 = n - 1

                if r1 < r0:
                    continue

            if r1 < l:
                continue
            if r0 < l:
                r0 = l

            need = k * k

            ones_at_r1 = po[r1 + 1] - po[l]
            if ones_at_r1 < need:
                continue

            lo, hi = r0, r1
            ans_r = r1
            while lo <= hi:
                mid = (lo + hi) // 2
                ones_mid = po[mid + 1] - po[l]
                if ones_mid >= need:
                    ans_r = mid
                    hi = mid - 1
                else:
                    lo = mid + 1

            total += (r1 - ans_r + 1)

    return total

print(xyz(s))