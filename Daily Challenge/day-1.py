m = 2
n = 2
original = [1,2,3,4]         


def start(original,m,n):
    x = m*n
    new_arr = [[None] * n for _ in range(m)]
    if (x == len(original)):
        
        for i in range(m):
            for j in range(n):
                new_arr[i][j] = original[i * n + j]
        return new_arr
    else:
        return new_arr
    
print(start(original,m,n))