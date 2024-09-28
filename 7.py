n = 120

def xyz(x):
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    
    sign = -1 if x < 0 else 1
    x_abs_reversed = int(str(abs(x))[::-1])
    
    result = sign * x_abs_reversed
    
    if result < INT_MIN or result > INT_MAX:
        return 0
    
    return result

print(xyz(n))