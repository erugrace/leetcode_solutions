class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = float("-inf")
        left = 0
        right = len(height)-1
        while left < right:
            area = (right - left) * min(height[left], height[right])
            maxArea = max(maxArea, area)
            if height[left]<height[right]:
                left += 1
            else:
                right-=1 
        return maxArea
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna