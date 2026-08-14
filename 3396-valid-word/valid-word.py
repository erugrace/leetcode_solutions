class Solution:
    def isValid(self, word: str) -> bool:
        vowels = {"a", "e", "i", "o", "u"}
        has_vowels = False
        has_consonants = False
        if len(word)< 3:
            return False 
        for char in word.lower():
            if not char.isalnum():
                return False
            if char.isalpha():
                if char in vowels:
                   has_vowels = True
                else:
                    has_consonants = True
        return has_vowels and has_consonants


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna