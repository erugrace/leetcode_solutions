class Solution:
    def countBits(self, n: int) -> List[int]:
        lst = []
        for num in range(0,n+1):
            binary = bin(num)
            lst.append(binary.count("1"))
        return lst
            
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna