# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        left = 0
        right = len(nums)-1
        def dfs(left,right):
            if left>right:
                return None
            mid = (left + right)//2
            node = TreeNode(nums[mid])
            node.left = dfs(left,mid-1)
            node.right = dfs(mid+1, right)
            return node
        return dfs(left,right)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna