# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> tuple[int,int]:
            if not node:
               return 0,0
            left_depth, left_dia = dfs(node.left)
            right_depth, right_dia = dfs(node.right)

            curr_depth=max(left_depth,right_depth)+1
            curr_dia=max(left_depth+right_depth,left_dia,right_dia)

            return curr_depth, curr_dia
        return dfs(root)[1]
        