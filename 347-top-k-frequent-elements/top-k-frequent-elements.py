class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num,0)
        res = []
        for num,i in count.items():
            res.append([i,num])
        res.sort()
        result = []
        while len(result) < k:
            result.append(res.pop()[1])
        return result


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna