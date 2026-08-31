class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        numdict = {}
        result = []
        for num in nums:
            if num not in numdict:
                numdict[num] = 1
            else:
                numdict[num]+=1
        for key in numdict:
            if numdict[key] == 2:
                result.append(key)
        return result 

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna