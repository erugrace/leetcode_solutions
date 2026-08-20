class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in "+-/*":
                stack.append(int(t))
            else:
                b = stack.pop()
                a = stack.pop()
                r  = 0
                if t == "+": r = a+ b
                elif t == "-": r = a - b
                elif t == "*": r = a*b
                else: r = int(a/b)
                stack.append(r)
        return stack[0] 
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna