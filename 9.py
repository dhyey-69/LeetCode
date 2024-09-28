# Given an integer x, return true if x is a palindrome and false otherwise.
# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

n = 121
m = 120

def xyz(num):
    flag = False
    temp = num
    sum = 0
    while(temp > 0):
        digit = temp % 10
        temp = temp // 10
        sum = (sum * 10) + digit
        print(sum)
    
    print(sum)
    if sum == num:
        flag = True
    
    return flag


print(xyz(n))