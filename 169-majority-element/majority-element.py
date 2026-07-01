class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        for num in nums:
            if num not in dict:
                dict[num] = nums.count(num)
            else:
                pass
        maxV = max(dict.values())
        for key in dict.keys():
            if dict[key] == maxV:
                return key

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna