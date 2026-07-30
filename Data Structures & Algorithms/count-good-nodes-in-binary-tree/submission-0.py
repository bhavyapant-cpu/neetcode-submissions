# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count=0
        if root == None:
            return count
        count+=1
        
        queue=deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node.right:
                if node.right.val >= node.val:
                    count+=1
                else:
                    node.right.val=node.val
                queue.append(node.right)

            if node.left:
                if node.left.val >= node.val:
                    count+=1
                else:
                    node.left.val=node.val
                queue.append(node.left)
        return count



        