class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        if num % 9 == 0:
            return 9
        else:
            return num % 9

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna