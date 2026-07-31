class Solution:
    def isPalindrome(self, s: str) -> bool:
        news = ""
        for char in s:
            if char.isalnum():
                char = char.lower()
                news = news + char
        if news == news[::-1]:
            return True
        else:
            return False

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna