# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorder(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        return self.inorder(root.left) + [root.val] + self.inorder(root.right)

        return arr
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        arr=self.inorder(root)
        for i in range(1,len(arr)):
            if arr[i-1]>=arr[i]:
                return False
        return True

        
        