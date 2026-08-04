class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        op = {"+", "-", "*"}
        def dfs(expr):
            results = []
            if not any(c in op for c in expr):
                return [int(expr)]
            for i,char in enumerate(expr):
                if char in op:
                    l = dfs(expr[:i])
                    r = dfs(expr[i+1:])
                    for i in l:
                        for j in r:
                            if char == "-":
                                results.append(i - j)
                            elif char == "+":
                                results.append(i + j)
                            else:
                                results.append(i * j)
            return results
        return dfs(expression)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna