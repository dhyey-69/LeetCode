# 1277. Count Square Submatrices with All Ones

# Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

 

# Example 1:

# Input: matrix =
# [
#   [0,1,1,1],
#   [1,1,1,1],
#   [0,1,1,1]
# ]
# Output: 15
# Explanation: 
# There are 10 squares of side 1.
# There are 4 squares of side 2.
# There is  1 square of side 3.
# Total number of squares = 10 + 4 + 1 = 15.
# Example 2:

# Input: matrix = 
# [
#   [1,0,1],
#   [1,1,0],
#   [1,1,0]
# ]
# Output: 7
# Explanation: 
# There are 6 squares of side 1.  
# There is 1 square of side 2. 
# Total number of squares = 6 + 1 = 7.
 

# Constraints:

# 1 <= arr.length <= 300
# 1 <= arr[0].length <= 300
# 0 <= arr[i][j] <= 1

# m = [[0,1,1,1],[1,1,1,1],[0,1,1,1]]
m = [[1,0,1],[1,1,0],[1,1,0]]

def xyz(matrix):
    total_squares = 0
        
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1 and i > 0 and j > 0:
                matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1
            
            total_squares += matrix[i][j]
        
    return total_squares

print(xyz(m))