# Largest Number

# Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

# Since the result may be very large, so you need to return a string instead of an integer.

 

# Example 1:

# Input: nums = [10,2]
# Output: "210"
# Example 2:

# Input: nums = [3,30,34,5,9]
# Output: "9534330"

n = [34323,3432]

def xyz(nums):

    # my_dict = {value % 10: value for value in n}

    # sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[0], reverse=True))
    
    # s = ""

    # for i in sorted_dict.values():
    #     s = s + str(i)

    # print("343234323")
    # return s


    nums_str = [str(num) for num in nums]
    
    nums_str.sort(key=lambda a: a*10, reverse=True)

    s = ""
    for i in nums_str:
        s += i

    if s[0] == '0':
        return '0'
    
    return s

print(xyz(n))