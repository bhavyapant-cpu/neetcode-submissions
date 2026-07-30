# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        if root == None:
            return ans
        
        queue=deque()
        queue.append(root)
        queue.append(None)

        while queue:
            node=queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
            if queue[0]==None:
                queue.popleft()
                ans.append(node.val)
                if len(queue):
                    queue.append(None)
        return ans

        