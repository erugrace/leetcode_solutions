class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for char in s:
            if char not in count:
                count[char] = 1
            else:
                count[char] += 1

        for char in t:
            if char not in count:
                return False

            count[char] -= 1

            if count[char] < 0:
                return False

        return True

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna