class Solution:
    def isHappy(self, n: int) -> bool:

        lst = list(str(n))
        seen = set()
      
        while True: 
            total = 0
            for num in lst:
               total += (int(num) * int(num))
            if total == 1:
                return True
            if total in seen:
                return False
            seen.add(total)
            lst = list(str(total))
       

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna