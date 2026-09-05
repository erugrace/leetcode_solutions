class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {"a", "e", "i", "o", "u"}
        v = []
        for char in s:
            if char.lower() in vowels:
                v.append(char)
        s = list(s)
        for i,char in enumerate(s):
            if char.lower() in vowels and v:
                s[i] = v.pop()
        return "".join(s)


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna