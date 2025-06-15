# 1432. Max Difference You Can Get From Changing an Integer
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are given an integer num. You will apply the following steps to num two separate times:

# Pick a digit x (0 <= x <= 9).
# Pick another digit y (0 <= y <= 9). Note y can be equal to x.
# Replace all the occurrences of x in the decimal representation of num by y.
# Let a and b be the two results from applying the operation to num independently.

# Return the max difference between a and b.

# Note that neither a nor b may have any leading zeros, and must not be 0.

 

# Example 1:

# Input: num = 555
# Output: 888
# Explanation: The first time pick x = 5 and y = 9 and store the new integer in a.
# The second time pick x = 5 and y = 1 and store the new integer in b.
# We have now a = 999 and b = 111 and max difference = 888
# Example 2:

# Input: num = 9
# Output: 8
# Explanation: The first time pick x = 9 and y = 9 and store the new integer in a.
# The second time pick x = 9 and y = 1 and store the new integer in b.
# We have now a = 9 and b = 1 and max difference = 8
 

# Constraints:

# 1 <= num <= 108

n = 855
# n = 9

def xyz(num):
    s = list(str(num))

    a_digits = s[:]
    for ch in a_digits:
        if ch != '9':
            target = ch
            break
    else:
        a_val = num
    if 'target' in locals():
        a_digits = ['9' if d == target else d for d in a_digits]
        a_val = int(''.join(a_digits))

    b_digits = s[:]
    first = b_digits[0]

    if first != '1':
        target = first
        replace_with = '1'
    else:
        target = None
        for d in b_digits[1:]:
            if d not in ('0', '1'):
                target = d
                replace_with = '0'
                break
    if target is not None:
        b_digits = [replace_with if d == target else d for d in b_digits]
    b_val = int(''.join(b_digits))

    return a_val - b_val

print(xyz(n))