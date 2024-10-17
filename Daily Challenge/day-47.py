# 670. Maximum Swap

# You are given an integer num. You can swap two digits at most once to get the maximum valued number.

# Return the maximum valued number you can get.

 

# Example 1:

# Input: num = 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.
# Example 2:

# Input: num = 9973
# Output: 9973
# Explanation: No swap.
 

# Constraints:

# 0 <= num <= 108

n = 2736
# n = 9973

def xyz(num):
    digits = list(str(num))        
    last = {int(d): i for i, d in enumerate(digits)}
        
    for i, d in enumerate(digits):
        for digit in range(9, int(d), -1):
            if last.get(digit, -1) > i:
                digits[i], digits[last[digit]] = digits[last[digit]], digits[i]
                return int(''.join(digits))
        
    return num

print(xyz(n))