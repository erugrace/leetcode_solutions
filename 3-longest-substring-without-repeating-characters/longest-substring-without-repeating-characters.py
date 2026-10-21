class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left  = 0
        maxS= 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[r])
            maxS = max(maxS,len(seen) )
        return maxS
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna