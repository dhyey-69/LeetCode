s1 = "BeHold"

def xyz(s):
    if s == "":
        return ""
    
    s = s.upper()

    d1 = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 
    'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 
    'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 
    'Z': 26
}
    
    r = []
    temp = ""

    for i in s:
        if i in d1:
            r.append(i)

    r = sorted(r)

    for i in r:
        temp = temp + str(i)

    return temp
xyz(s1)