class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> tuple[int, int]:
            if not node:
                return 0, 0  # (depth, diameter)
            
            left_depth, left_dia = dfs(node.left)
            right_depth, right_dia = dfs(node.right)
            
            # Current node's depth and maximum diameter seen so far
            current_depth = 1 + max(left_depth, right_depth)
            current_dia = max(left_depth + right_depth, left_dia, right_dia)
            
            return current_depth, current_dia

        return dfs(root)[1]