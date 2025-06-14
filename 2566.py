# 2566. Maximum Difference by Remapping a Digit
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given an integer num. You know that Bob will sneakily remap one of the 10 possible digits (0 to 9) to another digit.

# Return the difference between the maximum and minimum values Bob can make by remapping exactly one digit in num.

# Notes:

# When Bob remaps a digit d1 to another digit d2, Bob replaces all occurrences of d1 in num with d2.
# Bob can remap a digit to itself, in which case num does not change.
# Bob can remap different digits for obtaining minimum and maximum values respectively.
# The resulting number after remapping can contain leading zeroes.
 

# Example 1:

# Input: num = 11891
# Output: 99009
# Explanation: 
# To achieve the maximum value, Bob can remap the digit 1 to the digit 9 to yield 99899.
# To achieve the minimum value, Bob can remap the digit 1 to the digit 0, yielding 890.
# The difference between these two numbers is 99009.
# Example 2:

# Input: num = 90
# Output: 99
# Explanation:
# The maximum value that can be returned by the function is 99 (if 0 is replaced by 9) and the minimum value that can be returned by the function is 0 (if 9 is replaced by 0).
# Thus, we return 99.
 

# Constraints:

# 1 <= num <= 108

n = 11891
# n = 90

def xyz(num):
    s = list(str(num))

    max_digits = s[:]
    for ch in max_digits:
        if ch != '9':
            target_max = ch
            break
    else:
        target_max = None
            
    if target_max is not None:
        max_digits = ['9' if d == target_max else d for d in max_digits]
    max_val = int(''.join(max_digits))

    min_digits = s[:]
    for ch in min_digits:
        if ch != '0':
            target_min = ch
            break
    else:
        target_min = None
    if target_min is not None:
        min_digits = ['0' if d == target_min else d for d in min_digits]
    min_val = int(''.join(min_digits))

    return max_val - min_val

print(xyz(n))