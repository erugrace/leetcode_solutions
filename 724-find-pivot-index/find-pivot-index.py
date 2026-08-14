class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = 0
        left = 0
        for num in nums:
            total+= num
        for i,num in enumerate(nums):
            right = total - left - num
            if left == right:
                return i
            left += num
            # print(right)
            
        return -1

        
        
        # for i in range(len(nums)):
        #     left = 0
        #     right = 0
        #     if i == 0:
        #         for l in range(i+1, len(nums)):
        #             right += nums[l]
        #     elif i == len(nums) -1:
        #         for k in range(0,i):
        #             left += nums[k]
        #     else:
        #         for k in range(0,i):
        #             left += nums[k]
        #         for l in range(i+1, len(nums)):
        #             right += nums[l]
        #     if left == right:
        #         return i
        #     i += 1
        # return -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna