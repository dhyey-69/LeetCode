n = [1,2,3,3,2,2]

def xyz(nums):
    # max_subarray = max(nums)
    
    # sub_array = []
    
    # for i in range(0, len(nums)):
    #     temp = nums[i]
    #     for j in range(len(nums)):
    #         if (temp & nums[j]) == max_subarray:
    #             sub_array.append(nums[i])
    #             if i != j:
    #                 sub_array.append(nums[j])


    # print(sub_array)

    
    # return len(sub_array)

    max_subarray = max(nums)
    sub_array = []
    temp_subarray = []
    
    for i in range(len(nums)):
        if nums[i] == max_subarray:
            temp_subarray.append(nums[i])
        else:
            if len(temp_subarray) > len(sub_array):
                sub_array = temp_subarray
            temp_subarray = []
    
    if len(temp_subarray) > len(sub_array):
        sub_array = temp_subarray

    print(sub_array)
    
    return len(sub_array)


print(xyz(n))