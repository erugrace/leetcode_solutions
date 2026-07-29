# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # Your implementation is correct! 
        # You have successfully implemented the Binary Search approach.
        # Time Complexity: O(log n) - Optimal, as we halve the search space each iteration.
        # Space Complexity: O(1) - Optimal, as we only use a few integer variables.
        if n == 0:
            return 0
        if isBadVersion(1) == True:
            return 1
        l = 1
        r = n
        while l < r:
            mid = (l + r)//2
            if isBadVersion(mid) == True:
                r = mid
            else:
                l = mid + 1
        return l
        # This solution meets the expected complexity. You can now click "Submit"!

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna