# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root == None:
            return 0
        queue=deque()
        
        queue.append(root)
        queue.append(None)
        depth=0

        while queue:
            flag=False
            node=queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if queue[0]==None:
                flag=True
                queue.popleft()        
            if flag:
                depth+=1
                if len(queue):
                    queue.append(None)
                flag=False
        return depth   
