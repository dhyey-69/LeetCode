n = [3,2,3]
aim = 6

def xyz(nums,target):
        num_dict = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in num_dict:
                return [num_dict[complement], i]
            
            num_dict[num] = i

print(xyz(n,aim))