class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix =1
        postfix = 1
        output = [1] * len(nums)
        for i in range(len(nums)):
            output[i] *= prefix
            prefix *= nums[i]
        for i in range(len(nums) -1, -1, -1):
            output[i ] *= postfix
            postfix *= nums[i]
        return output
        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna