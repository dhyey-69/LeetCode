from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def spiralMatrix(self, m: int, n: int, head: ListNode) -> List[List[int]]:
        arry = [[-1] * n for _ in range(m)]  
        
        row, col = 0, 0
        top, bottom, left, right = 0, m - 1, 0, n - 1  # Boundary
        direction = 0  # 0: right, 1: down, 2: left, 3: up

        while head:
            arry[row][col] = head.val
            
            head = head.next
            
            if direction == 0:  # Moving right
                if col < right:
                    col += 1
                else:
                    top += 1
                    row += 1
                    direction = 1
            elif direction == 1:  # Moving down
                if row < bottom:
                    row += 1
                else:
                    right -= 1
                    col -= 1
                    direction = 2
            elif direction == 2:  # Moving left
                if col > left:
                    col -= 1
                else:
                    bottom -= 1
                    row -= 1
                    direction = 3
            elif direction == 3:  # Moving up
                if row > top:
                    row -= 1
                else:
                    left += 1
                    col += 1
                    direction = 0

        return arry
    

def create_linked_list(lst):
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


m = 3
n = 5
ll = [3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0]
linked_list = create_linked_list(ll)

sol = Solution()
result = sol.spiralMatrix(m, n, linked_list)
for row in result:
    print(row)
