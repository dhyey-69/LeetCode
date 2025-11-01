from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums_set = set(nums)
        temp = ListNode(0)
        temp.next = head
        current = temp
        
        while current and current.next:
            if current.next.val in nums_set:
                current.next = current.next.next
            else:
                current = current.next

        return temp.next

# Utility functions for testing:

# Converts a list to a linked list
def list_to_linked_list(lst: List[int]) -> Optional[ListNode]:
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Converts a linked list back to a list
def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    lst = []
    current = head
    while current:
        lst.append(current.val)
        current = current.next
    return lst

# Example test case
n = [5, 10, 15]  # Elements to be removed
h = [1, 5, 2, 10, 3, 15, 4]  # Linked list elements

# Convert the list to a linked list
linked_list = list_to_linked_list(h)

# Create a Solution instance and modify the linked list
solution = Solution()
modified_head = solution.modifiedList(n, linked_list)

# Convert the modified linked list back to a list and print it
print(linked_list_to_list(modified_head))
