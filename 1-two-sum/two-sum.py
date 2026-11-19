class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        complement = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in complement:
                return [min(i,complement[diff]), max(i,complement[diff])]
            else:
                complement[nums[i]] = i
        
            
            
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna