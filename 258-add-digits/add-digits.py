class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            total = 0

            while num > 0:
                # Get the last digit
                last = num % 10
                # Add it to total
                total += last
                # Remove the last digit
                num = num // 10

            num = total

        return num

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna