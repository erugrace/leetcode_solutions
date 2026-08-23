class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1,rob2 = 0,0
        for money in nums:
            temp = max(rob2,rob1 + money)
            rob1 = rob2
            rob2 = temp
        return rob2


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna