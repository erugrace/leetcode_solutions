class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = 0
        a,b = a[::-1], b[::-1]
        for i in range(max(len(a),len(b))):
            digit1 = int(a[i]) if i < len(a) else 0
            digit2 = int(b[i]) if i <len(b) else 0
            total = digit1 + digit2 + carry
            res = str(total % 2) + res 
            carry = total // 2
        if carry:
            res = str(carry) + res


        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna