a = "ab"
w = ["ad","bd","aaab","baa","badab"]

def xyz(allowed,word):
    allowed_set = set(allowed)
    count  = 0
            
    for w in word:
        if all(char in allowed_set for char in w):
            count += 1
            
    return count


print(xyz(a,w))

# Design a function to find the longest substring that ouccrens at least twice in given string 
# Example : banana
# output