a1 = [1,10,100]
# a1 = [1,2,3]
a2 = [1000]
# a2 = [4,4,4]

def xyz(arr1,arr2):
    prefix1 = []
    prefix2 = []
    
    
    for i in arr1:
        temp1 = ""
        for j in str(i):
            temp1 = temp1 + j
            prefix1.append(temp1)

    
    prefix1 = set(prefix1)
    
    for i in arr2:
        temp2 = ""
        for j in str(i):
            temp2 = temp2 + j
            prefix2.append(temp2)

    prefix2 = set(prefix2)

    inter = prefix1.intersection(prefix2)
    
    current_l = 0
    max_l = current_l

    for i in inter:
        current_l = len(i)
        if current_l > max_l:
            max_l = current_l


    return max_l
        
    

print(xyz(a1,a2))