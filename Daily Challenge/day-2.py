chalk = [5,1,5]
k = 25

def xyz(chalk,k):
    i = 0
    while(k > 0):
        for i in range(len(chalk)):
            if k < chalk[i]:
                return i
            k -= chalk[i]
    return i
        
x = xyz(chalk,k)
print(x)