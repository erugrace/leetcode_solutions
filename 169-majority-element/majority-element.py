class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        diction = {}
        for num in nums:
            if num not in diction:
                diction[num] = 1
            else:
                diction[num]+=1
        maxNum = max(diction.values())
        for key in diction.keys():
            if diction[key] == maxNum:
                return key
        
     

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna