class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) -1
        while left < right:
            nsum = numbers[right] + numbers[left]
            if nsum == target:
                return [left+1,right+1]
            elif nsum < target:
                left += 1
            else:
                right -= 1
        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna