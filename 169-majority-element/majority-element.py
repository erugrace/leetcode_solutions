class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res,count = 0,0
        for num in nums:
            if count == 0:
                res = num
            count += (1 if res == num else -1)
        return res
        
     

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna