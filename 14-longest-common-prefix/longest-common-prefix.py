class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        dict = {}
        for i in range(len(strs)):
            dict[i] = len(strs[i])
        minlength = min(dict.values())
        for key,value in dict.items(): 
            if value == minlength:
                minindex = key

        prefix = ""
        for i in (range(len(strs[minindex]))):
            for j in range(1, len(strs)):
                if strs[j][i] != strs[0][i]:
                    return prefix
            prefix= prefix + strs[0][i]
        return prefix
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna