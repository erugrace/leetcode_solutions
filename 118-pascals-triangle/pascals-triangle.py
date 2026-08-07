class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = []
        
        for i in range(numRows):
            row = [1] * (i+1)
            for j in range(1,i):
                prev_row = pascal[-1]
                row[j] = prev_row[j] + prev_row[j-1]
            pascal.append(row)
        return pascal
                

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna