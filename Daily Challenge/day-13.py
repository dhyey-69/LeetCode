a = [4,8,2,10]
# a = [1,3,4,8]
# q = [[0,1],[1,2],[0,3],[3,3]]
q = [[2,3],[1,3],[0,0],[0,3]]

def xyz(arr,queries):
    # result = []

    # for i in quiers:
    #     left = i[0]
    #     right = i[1]
        
    #     if(left == right):
    #         result.append(arr[left])
    #     else:
    #         r = arr[left]
    #         while left < right:
    #             r = r ^ arr[left+1]
    #             left += 1

    #         result.append(r)

    # return result

    arr_XOR = [0] * (len(arr) + 1)
    
    for i in range(1, len(arr) + 1):
        arr_XOR[i] = arr_XOR[i - 1] ^ arr[i - 1]

    result = []

    for i in queries:
        left = i[0]
        right = i[1]

        result.append(arr_XOR[right + 1] ^ arr_XOR[left])

    return result

print(xyz(a,q))