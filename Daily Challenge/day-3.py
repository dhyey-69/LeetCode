str = "vbyytoijnbgtyrjlsc"
k=2

def xyz(s,k):
    l = list(s)
    print(l)
    sum = 0
    alphabet_dict = {chr(i): i - 96 for i in range(97, 123)}

    for j in l:
        if j in alphabet_dict:
            if alphabet_dict.get(j) > 9:
                a = alphabet_dict.get(j)
                second_digit = a % 10
                first_digit = int((a-second_digit) / 10)
                sum += first_digit
                sum += second_digit
            else:
                sum += alphabet_dict.get(j)
    k -= 1
    while(k > 0):
        if sum > 9:
            while sum > 9:
                a = sum
                second_digit = a % 10
                first_digit = int((a-second_digit) / 10)
                print("First Digit:", first_digit)
                print("Second Digit:", second_digit)
                sum = 0
                sum += second_digit
                sum += first_digit
                k -= 1
                if(k == 0):
                    break
        else:   
            k -= 1

        # for j in l:
        #     if j in alphabet_dict:
        #         a = alphabet_dict.get(j)
        #         if a > 9:
        #             while a > 0:
        #                 sum += a % 10
        #                 a //= 10
        #     else:
        #         sum += a
        # for _ in range(k - 1):
        #     temp_sum = 0
        #     while sum > 0:
        #         temp_sum += sum % 10
        #         sum //= 10
        #     sum = temp_sum

    return sum

print(xyz(str,k))