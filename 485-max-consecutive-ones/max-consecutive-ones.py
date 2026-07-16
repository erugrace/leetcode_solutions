class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxf = 0
        count = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                maxf = max(maxf, count)
                count = 0
        return max(count, maxf)
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna