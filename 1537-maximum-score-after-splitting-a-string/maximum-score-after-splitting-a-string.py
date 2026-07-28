class Solution:
    def maxScore(self, s: str) -> int:
        left = 0
        right = len(s)
        lst =[]
        m =1
        while m < right:
            lefts = s[left:m].count("0")
            rights = s[m:len(s)].count ("1")
            lst.append(lefts+ rights)
            m += 1
        return max(lst)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna