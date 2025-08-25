# 498. Diagonal Traverse
# Medium
# Topics
# premium lock icon
# Companies
# Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

 

# Example 1:


# Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,4,7,5,3,6,8,9]
# Example 2:

# Input: mat = [[1,2],[3,4]]
# Output: [1,2,3,4]
 

# Constraints:

# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 104
# 1 <= m * n <= 104
# -105 <= mat[i][j] <= 105


m = [[1,2,3],[4,5,6],[7,8,9]]
# m = [[1,2],[3,4]]

def xyz(mat):
    if not mat or not mat[0]:
        return []
    
    m, n = len(mat), len(mat[0])
    result = []
    
    for d in range(m + n - 1):
        temp = []
        
        r = 0 if d < n else d - n + 1
        c = d if d < n else n - 1
        
        while r < m and c >= 0:
            temp.append(mat[r][c])
            r += 1
            c -= 1
        
        if d % 2 == 0:
            result.extend(temp[::-1])
        else:
            result.extend(temp)
    
    return result

print(xyz(m))