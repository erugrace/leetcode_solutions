class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        placeholder  = val + 1
        l = 0 
        for r in range(len(nums)):
            if nums[r] != val:
                nums[l],nums[r] = nums[r],nums[l]
                l += 1
        return l

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna