# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxVal = 0
        def dfs(node):
            nonlocal maxVal
            if not node:
               return -1
            left  = dfs(node.left)
            right = dfs(node.right)
            maxVal  = max(maxVal, left + right + 2)
            return 1 + max(left, right)
        dfs(root)
        return maxVal 

                 

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna