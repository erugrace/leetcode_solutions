# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        def dfs(node):
            if not node:
                return [True, 0]
            left,right = dfs(node.left) , dfs(node.right)
            balanced = abs(left[1] - right[1]) <= 1 and left[0] and right[0]
            return [balanced, 1+ max(left[1], right[1])]
        return dfs(root)[0]
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna