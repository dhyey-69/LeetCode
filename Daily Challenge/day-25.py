w = ["abc","ab","bc","b"]

def xyz(words):
    answer = []
    
    for i in w:
        temp = ""
        prefix = []
        for j in str(i):
            temp = temp + str(j)
            prefix.append(temp)
        
        total = 0
        for j in prefix:
            count = 0
            for k in range(len(words)):
                if str(words[k]).startswith(j):
                    count += 1
            total += count
        
        answer.append(total)
    
    return answer

print(xyz(w))