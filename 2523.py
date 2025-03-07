# 2523. Closest Prime Numbers in Range
# Medium
# Topics
# Companies
# Hint
# Given two positive integers left and right, find the two integers num1 and num2 such that:

# left <= num1 < num2 <= right .
# Both num1 and num2 are prime numbers.
# num2 - num1 is the minimum amongst all other pairs satisfying the above conditions.
# Return the positive integer array ans = [num1, num2]. If there are multiple pairs satisfying these conditions, return the one with the smallest num1 value. If no such numbers exist, return [-1, -1].

 

# Example 1:

# Input: left = 10, right = 19
# Output: [11,13]
# Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
# The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
# Since 11 is smaller than 17, we return the first pair.
# Example 2:

# Input: left = 4, right = 6
# Output: [-1,-1]
# Explanation: There exists only one prime number in the given range, so the conditions cannot be satisfied.
 

# Constraints:

# 1 <= left <= right <= 106

l = 10
r = 19

# l = 4
# r = 6

def isprime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True


def xyz(left,right):
    prime_num = []
    if left <= 2 and right >= 2:
        prime_num.append(2)

    if left % 2 == 0:
        left += 1

    for i in range(left, right + 1, 2):
        if isprime(i):
            prime_num.append(i)

    if len(prime_num) < 2:
        return [-1,-1]
    
    elif len(prime_num) == 2:
        return prime_num
    
    else:
        dif = float('inf')
        res = [prime_num[0] , prime_num[1]]
        for i in range(len(prime_num) - 1):
            if (prime_num[i+1] - prime_num[i]) < dif:
                dif = prime_num[i+1] - prime_num[i]
                res = [prime_num[i] , prime_num[i+1]]
            
            elif dif == prime_num[i+1] - prime_num[i]:
                if prime_num[i] < res[0]:
                    res = [prime_num[i] , prime_num[i+1]]
        
        return res
    
print(xyz(l,r))