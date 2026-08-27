class Solution:
    def isBalanced(self, num: str) -> bool:
        odd = 0
        even = 0
        for i in range(len(num)):
            if i % 2 == 0:
                even += int(num[i])
            else:
                odd+=int(num[i])
        return odd == even 
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna