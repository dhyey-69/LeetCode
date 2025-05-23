# 1019. Next Greater Node In Linked List
# Medium
# Topics
# Companies
# Hint
# You are given the head of a linked list with n nodes.

# For each node in the list, find the value of the next greater node. That is, for each node, find the value of the first node that is next to it and has a strictly larger value than it.

# Return an integer array answer where answer[i] is the value of the next greater node of the ith node (1-indexed). If the ith node does not have a next greater node, set answer[i] = 0.

 

# Example 1:


# Input: head = [2,1,5]
# Output: [5,5,0]
# Example 2:


# Input: head = [2,7,4,3,5]
# Output: [7,0,5,5,0]
 

# Constraints:

# The number of nodes in the list is n.
# 1 <= n <= 104
# 1 <= Node.val <= 109

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nextLargerNodes(self, head):
        values = []
        while head:
            values.append(head.val)
            head = head.next
        
        n = len(values)
        result = [0] * n
        stack = []
        
        for i in range(n):
            while stack and values[stack[-1]] < values[i]:
                index = stack.pop()
                result[index] = values[i]
            stack.append(i)
        
        return result

s = Solution()
head = [2,1,5]
s.nextLargerNodes(head)