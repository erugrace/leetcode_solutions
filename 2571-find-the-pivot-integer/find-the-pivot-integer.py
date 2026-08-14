class Solution:
    def pivotInteger(self, n: int) -> int:
        total = 0
        left = 0
        for n in range(n+1):
            total += n
        for n in range(1,n+1):
            left += n
            right = total - left + n
            if left == right:
                return n
        return -1
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna