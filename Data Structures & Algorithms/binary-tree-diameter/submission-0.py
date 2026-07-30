# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter=0
        if root ==None:
            return max_diameter
        def calcdepth(root:Optional[TreeNode]) -> int:
            d1=0
            d2=0
            nonlocal max_diameter

            if root==None:
                return 0

            if root.left:
                d1=calcdepth(root.left)+1
            if root.right:
                d2=calcdepth(root.right)+1

            max_diameter=max(max_diameter,d1+d2)
            return max(d1,d2)
        calcdepth(root)
        return max_diameter
        