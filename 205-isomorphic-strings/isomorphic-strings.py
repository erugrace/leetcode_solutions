class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}
        for charS , charT in zip(s,t):
            if charS in s_to_t:
                if s_to_t[charS] != charT:
                    return False
            if charT in t_to_s:
                if t_to_s[charT] != charS:
                    return False
            s_to_t[charS] = charT
            t_to_s[charT] = charS
        return True 

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna