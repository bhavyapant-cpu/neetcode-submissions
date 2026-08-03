# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p==None or q==None or root == None:
            return None
        
        queue=deque()
        queue.append(root)

        if q.val < p.val:
            p,q=q,p

        while queue:
            node=queue.popleft()
            if p.val <= node.val <= q.val:
                return node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
        return None
        