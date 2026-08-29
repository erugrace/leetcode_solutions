class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = {}
        for char in s:
            if char not in dict:
                dict[char] = 1
            else:
                dict[char] += 1
        for i in range(len(s)):
            if dict[s[i]] == 1:
                return i

        return -1 
            
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna