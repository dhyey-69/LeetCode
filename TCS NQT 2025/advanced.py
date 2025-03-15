def xyz(L, i=None, j=None):
    if i is None or j is None:
        return "Missing Input"
    
    if (i < 0 or i > j or i >= 10000) or (j < 0 or j < i or j >= 10000):
        return "Not Valid Range of Input"
    
    return sum(L[i:j+1])  

L = [i for i in range(0, 10000)]

print(xyz(L, 500, 1000))

print(xyz(L, 500, 100000))

print(xyz(L, None, 1000))
print(xyz(L, 500))
print(xyz(L))
