class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for l in range(len(nums)):
            for r in (range((l+1), len(nums))):
                if nums[l] + nums[r] == target:
                    return [l,r]
            
            
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna