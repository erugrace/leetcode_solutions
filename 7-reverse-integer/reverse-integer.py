class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            newx = -1 * (x)
        else:
            newx = x
        integers = ["1","2","3","4","5","6","7","8","9","10"]
        newS = ""
        newx = str(newx)
        
        for i in range(len(newx)):
            newS =newx[i] + newS
        newS = int(newS)
        if x < 0:
            newS = -1 * newS
        if newS < -2**31 or newS > 2**31 - 1:
           return 0
        return newS
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna