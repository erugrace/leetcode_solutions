class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1, num2 = num1[::-1], num2[::-1]
        carry = 0
        res = ""
        for i in range(max(len(num1), len(num2))):
            digitA = int(num1[i]) if i < len(num1) else 0
            digitB = int(num2[i]) if i < len(num2) else 0
            total = digitA + digitB + carry
            res = str(total % 10) + res
            carry = total // 10
        if carry:
            res = str(carry) + res
        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna