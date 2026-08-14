class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        op = {"+", "-", "*"}
        def dfs(expr):
            res = []
            if not any (c in op for c in expr):
                return [int(expr)]
            for i,char in enumerate(expr):
                if char in op:
                    left = dfs(expr[:i])
                    right = dfs(expr[i+1:])
                    for l in left:
                        for r in right:
                            if char == "*":
                                res.append(l*r)
                            if char == "+":
                                res.append(l+r)
                            if char == "-":
                                res.append(l-r)
            return res
        return dfs(expression)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna