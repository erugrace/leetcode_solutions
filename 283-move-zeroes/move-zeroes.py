class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # NOTE: This implementation does NOT preserve the relative order of non-zero elements.
        # The algorithm starts scanning from r=1, which causes a swap that may reorder
        # non-zero elements when the first element is non-zero. For example, [1,0,2]
        # becomes [2,0,1] instead of the correct [1,2,0].
        # To fix this, start r from 0 (or use a separate index for the next
        # position to place a non-zero element) and increment l only when a
        # non-zero is encountered.
        # Time Complexity: O(n) where n is the length of nums.
        # Space Complexity: O(1) auxiliary space.
        
        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna