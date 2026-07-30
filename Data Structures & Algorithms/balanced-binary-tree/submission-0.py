# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root:Optional[TreeNode]) -> tuple[int,bool]:
            if not root:
                return 0,True
            
            left_depth, balanced_left = dfs(root.left)
            right_depth, balanced_right =  0, False
            if not balanced_left:
                return 0,False
            right_depth, balanced_right = dfs(root.right)
            if not balanced_right:
                return 0,False
            
            balanced=True if abs(left_depth-right_depth)<=1 else False

            return max(left_depth,right_depth)+1,balanced
        return dfs(root)[1]


        