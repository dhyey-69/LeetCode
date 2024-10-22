# 2583. Kth Largest Sum in a Binary Tree

# You are given the root of a binary tree and a positive integer k.

# The level sum in the tree is the sum of the values of the nodes that are on the same level.

# Return the kth largest level sum in the tree (not necessarily distinct). If there are fewer than k levels in the tree, return -1.

# Note that two nodes are on the same level if they have the same distance from the root.

 

# Example 1:


# Input: root = [5,8,9,2,1,3,7,4,6], k = 2
# Output: 13
# Explanation: The level sums are the following:
# - Level 1: 5.
# - Level 2: 8 + 9 = 17.
# - Level 3: 2 + 1 + 3 + 7 = 13.
# - Level 4: 4 + 6 = 10.
# The 2nd largest level sum is 13.
# Example 2:


# Input: root = [1,2,null,3], k = 1
# Output: 3
# Explanation: The largest level sum is 3.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthLargestLevelSum(self, root: TreeNode, k: int) -> int:
        if not root:
            return -1
        
        queue = [root]
        level_sums = []
        
        while queue:
            level_sum = 0
            next_queue = []
            
            for node in queue:
                level_sum += node.val
                
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            
            level_sums.append(level_sum)
            queue = next_queue
        
        level_sums.sort(reverse=True)
        
        if k <= len(level_sums):
            return level_sums[k-1]
        else:
            return -1


root = TreeNode(5)
root.left = TreeNode(8)
root.right = TreeNode(9)
root.left.left = TreeNode(2)
root.left.right = TreeNode(1)
root.right.left = TreeNode(3)
root.right.right = TreeNode(7)
root.left.left.left = TreeNode(4)
root.left.left.right = TreeNode(6)

k = 2

a = Solution()
print(a.kthLargestLevelSum(root, k))