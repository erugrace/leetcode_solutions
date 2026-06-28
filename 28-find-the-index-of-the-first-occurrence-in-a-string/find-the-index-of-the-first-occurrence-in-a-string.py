class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        end = len(haystack) -1
        e = len(needle) -1
        b= 0
        while e <= end:
            if haystack[b:e+1] == needle:
                return b
            b += 1
            e+= 1
        return -1


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna