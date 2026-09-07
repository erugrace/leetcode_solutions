class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        output = []
        for i in matrix:
            count = 0
            for j in i:
                if j == 1:
                    count += 1
            output.append(count)
        return output

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna