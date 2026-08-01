class Solution:
    def isValid(self, word: str) -> bool:
        vowels = {"a", "e", "i", "o", "u"}

        if len(word) < 3:
            return False

        has_vowel = False
        has_consonant = False

        for s in word:
            if not s.isalnum():
                return False

            if s.isalpha():
                if s.lower() in vowels:
                    has_vowel = True
                else:
                    has_consonant = True

        return has_vowel and has_consonant
            
        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna