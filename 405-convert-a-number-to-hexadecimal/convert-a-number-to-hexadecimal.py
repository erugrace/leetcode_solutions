class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        hex_digits = "0123456789abcdef"

        # Convert to 32-bit unsigned integer
        num &= 0xffffffff

        result = ""

        while num > 0:
            remainder = num % 16
            result = hex_digits[remainder] + result
            num //= 16

        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna