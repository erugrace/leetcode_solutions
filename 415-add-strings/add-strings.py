class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1,num2 = num1[::-1], num2[::-1]
        res = ""
        carry = 0
        for i in range(max(len(num1), len(num2))):
            digit1 = int(num1[i]) if i < len(num1) else 0
            digit2 = int(num2[i]) if i < len(num2) else 0
            total = digit1 + digit2 + carry
            res = str(total % 10) + res
            carry = total // 10


        if carry:
            res = str(carry) + res
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna