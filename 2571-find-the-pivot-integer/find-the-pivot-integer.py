class Solution:
    def pivotInteger(self, n: int) -> int:
        total = 0
        for num in range(0,n+1):
            total += num
        left = 0
        for num in range(1,n+1):
            left += num
            right = total - left + num
            if left == right:
                return num
        return -1

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna