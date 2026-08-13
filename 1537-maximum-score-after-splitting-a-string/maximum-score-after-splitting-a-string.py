class Solution:
    def maxScore(self, s: str) -> int:
        maxS = 0
        l = 0
        for r in range(1,len(s)):
            left = s[l:r]
            right = s[r:]
            count = left.count("0") + right.count("1")
            maxS = max(count,maxS)
        return maxS

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna