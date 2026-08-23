class Solution:
    def rob(self, nums: List[int]) -> int:
        previous_previous = 0
        previous = 0

        for money in nums:
            current = max(previous, money + previous_previous)

            previous_previous = previous
            previous = current

        return previous

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna