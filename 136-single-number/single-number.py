class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict = {}
        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                dict[num] +=1
        for key in dict.keys():
            if dict[key] == 1:
                return key

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna