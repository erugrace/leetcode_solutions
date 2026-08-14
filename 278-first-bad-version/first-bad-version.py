# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 0:
            return 0
        left = 1
        right = n
        while left < right:
            mid = (left + right)//2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna