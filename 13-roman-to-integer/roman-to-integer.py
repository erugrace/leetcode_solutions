class Solution:
    def romanToInt(self, s: str) -> int:
        definition= {"I": 1, "V": 5, "X":10, "L": 50, "C":100, "D":500, "M":1000}
        total = 0
        for i in range(len(s)):
            if i < len(s) - 1 and definition[s[i]] < definition[s[i + 1]]:
                total -= definition[s[i]]
            else:
                total += definition[s[i]]
        return total

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna