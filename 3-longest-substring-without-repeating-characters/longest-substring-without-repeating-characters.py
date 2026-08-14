class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        l = 0
        result = 0
        for r in range(len(s)):
            if s[r] in charset:
                while s[r] in charset:
                    charset.remove(s[l])
                    l+= 1
            charset.add(s[r])
            result = max(result, r-l+1)
        return result
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna