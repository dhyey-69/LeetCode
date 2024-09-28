# Given the string s, return the size of the longest substring containing each vowel an even number of times. That is, 'a', 'e', 'i', 'o',
# and 'u' must appear an even number of times.
# Example 1:

# Input: s = "eleetminicoworoep"
# Output: 13
# Explanation: The longest substring is "leetminicowor" which contains two each of the vowels: e, i and o and zero of the vowels: a and u.

s = "eleetminicoworoep"

def xyz(str):
    # count_a, count_e, count_i, count_o, count_u = 0, 0, 0, 0, 0
    # vowels = ['a','e','i','o','u']
    # maxlen = 0

    # substrings = []
    # length = len(str)
    # for i in range(length):
    #     for j in range(i + 1, length + 1):
    #         substrings.append(str[i:j])
    
    # for i in substrings:
    #     print(i)
    #     for j in i:
    #         if j in vowels and j == 'a':
    #             count_a += 1
    #         elif j in vowels and j == 'e':
    #             count_e += 1
    #         elif j in vowels and j == 'i':
    #             count_i += 1
    #         elif j in vowels and j == 'o':
    #             count_o += 1
    #         elif j in vowels and j == 'u':
    #             count_u += 1
    #         else:
    #             pass
        
    #     if count_a % 2 == 0:
    #         if count_e % 2 == 0:
    #             if count_i % 2 == 0:
    #                 if count_o % 2 == 0:
    #                     if count_u % 2 == 0:
    #                         temp = len(i)
    #                         if temp > maxlen:
    #                             maxlen = temp
    #     count_a = 0
    #     count_e = 0
    #     count_i = 0
    #     count_o = 0
    #     count_u = 0
    
    # return maxlen

        count_a, count_e, count_i, count_o, count_u = 0, 0, 0, 0, 0
        maxlen = 0
        count_dict = {(0, 0, 0, 0, 0): -1}

        for index, char in enumerate(s):
            if char == 'a':
                count_a += 1
            elif char == 'e':
                count_e += 1
            elif char == 'i':
                count_i += 1
            elif char == 'o':
                count_o += 1
            elif char == 'u':
                count_u += 1

            vowel_counts = (count_a % 2, count_e % 2, count_i % 2, count_o % 2, count_u % 2)

            if vowel_counts in count_dict:
                maxlen = max(maxlen, index - count_dict[vowel_counts])
            else:
                count_dict[vowel_counts] = index
            print("Index",index)
            print("count_dict[vowel_counts] = ",count_dict[vowel_counts])
            print(count_dict)
            print("MaxLen = ",maxlen)

        return maxlen
            

print(xyz(s))