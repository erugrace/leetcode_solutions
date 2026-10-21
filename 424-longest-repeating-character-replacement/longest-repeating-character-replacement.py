class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l= 0
        chardict = {}
        for r in range(len(s)):
            chardict[s[r]] = 1 + chardict.get(s[r],0)
            if (r-l+1) -  max(chardict.values()) <= k:
                res = max(res, (r-l+1))
            else:
                chardict[s[l]] -=1
                l += 1
        return res

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna