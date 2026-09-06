class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def backtrack(i):
            if i == len(nums):
                result.append(subset.copy())
                return

            # choose nums[i]
            subset.append(nums[i])
            backtrack(i + 1)

            # don't choose nums[i]
            subset.pop()
            backtrack(i + 1)

        backtrack(0)
        return result
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna