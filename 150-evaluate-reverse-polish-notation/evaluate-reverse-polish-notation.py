class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
                if t in "+-*/":
                    left = stack.pop()
                    right = stack.pop()
                    if t == "+":
                        stack.append(int(right + left))
                    elif t == "-":
                        stack.append(int(right - left))
                    elif t == "*":
                        stack.append(int(right * left))
                    else:
                        stack.append(int(right / left))
                else:
                    stack.append(int(t))
        return stack[0]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna