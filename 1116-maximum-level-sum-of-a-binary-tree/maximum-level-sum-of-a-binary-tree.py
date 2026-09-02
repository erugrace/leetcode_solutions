# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            queue = deque([root])
            maxSum = float("-inf")
            level= 0
            ans = 0
            while queue:
                total = 0
                level_size = len(queue)
                for i in range(level_size):
                    node = queue.popleft()
                    total += node.val
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                level +=1
                
                if total > maxSum:
                    maxSum = total 
                    ans = level
                
            return ans
        return dfs(root)

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna