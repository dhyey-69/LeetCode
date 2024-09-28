r = [1,5,6]
m = 3
n = 4

def hello(rolls,mean,n):
    arr_n = []
    m = len(rolls)
    sum_of_rolls = sum(rolls)
    max_n_sum = n * 6
    min_n_sum = n * 1
    sum_of_unkown_elements = mean * (m+n)

    finding_required_sum = sum_of_unkown_elements - sum_of_rolls
    print(finding_required_sum)
               
    if finding_required_sum > max_n_sum or finding_required_sum < min_n_sum:
        return []
    else:
        for i in range(n):
            r = min(6, finding_required_sum - (n - 1 - i))
            arr_n.append(r)
            finding_required_sum -= r
        
        return arr_n

print(hello(r,m,n))