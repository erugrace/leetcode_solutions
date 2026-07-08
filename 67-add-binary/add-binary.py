class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        a,b = a[::-1], b[::-1]
        carry = 0
        for n in range(max(len(a), len(b))):
            digit1 = int(a[n]) if n < len(a) else 0
            digit2 = int(b[n]) if n < len(b) else 0
            total = digit1 + digit2 + carry
            res = str(total % 2) + res 
            carry= total // 2
        if carry: 
            res = str(carry) + res
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna