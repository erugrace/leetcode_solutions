class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ""
        for char in s:
            if char.isalnum():
                newS+= char.lower()
        reverse = newS[::-1]
        if newS == reverse:
            return True
        return False
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna