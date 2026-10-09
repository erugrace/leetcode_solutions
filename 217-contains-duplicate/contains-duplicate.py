class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        dict = {}
        for num in nums:
            if num not in dict:
                dict[num ] = 1
            else:
                return True
        return False

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna