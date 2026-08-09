class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:        
        res = ""
        for i in range(len(strs[0])):
            for j in strs:
                # Fix: Check length first to avoid IndexError
                if i == len(j) or j[i]!= strs[0][i] :
                    return res
            res = res + strs[0][i]
        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna