class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0 or (3 ** 19) % n != 0:
            return False
        return True
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna