# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxSum=-1001
    def findMaxPath(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return -1001
        maxLeft=self.findMaxPath(root.left)
        maxRight=self.findMaxPath(root.right)

        if maxLeft==-1001 and maxRight==-1001:
            self.maxSum=max(self.maxSum,root.val)
            return root.val
        if maxLeft==-1001:
            self.maxSum=max(self.maxSum,root.val,maxRight+root.val)
            return max(root.val,maxRight+root.val)
        if maxRight==-1001:
            self.maxSum=max(self.maxSum,root.val,maxLeft+root.val)
            return max(root.val,maxLeft+root.val)
        
        self.maxSum=max(self.maxSum,root.val,maxLeft+root.val,maxRight+root.val,maxLeft+maxRight+root.val)
        return max(root.val,maxLeft+root.val,maxRight+root.val)
        

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.findMaxPath(root)
        return self.maxSum
        
        