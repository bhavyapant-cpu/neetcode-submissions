# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        if root == None:
            return ans
        queue=deque()
        queue.append(root)
        queue.append(None)

        while queue:
            arr=[]
            while queue[0]!=None:
                node=queue.popleft()
                arr.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(arr)
            if queue[0]==None:
                queue.popleft()
                if len(queue):
                    queue.append(None)  
        return ans
             