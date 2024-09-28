n = 13
k = 2

def xyz(n,k):
    current_prefix = 1
    k -= 1
        
    while k > 0:
        count = countNumbersWithPrefix(current_prefix, n)
        if k >= count:
            current_prefix += 1
            k -= count
        else:
            current_prefix *= 10
            k -= 1
        
    return current_prefix

def countNumbersWithPrefix(prefix, n):
        first_number = prefix
        next_number = prefix + 1
        total_count = 0

        while first_number <= n:
            total_count += min(n + 1, next_number) - first_number
            first_number *= 10
            next_number *= 10

        return total_count



print(xyz(n,k))