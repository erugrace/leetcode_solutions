class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            m=(l+ r) // 2
            if nums[m] == target:
                return m
            
            # Hint: Check your boundary condition here.
            # If nums[l] == nums[m], the condition nums[l] < nums[m] fails.
            # In a 2-element array where nums[l] is the target, this might skip logic.
            # Change 'nums[l] < nums[m]' to 'nums[l] <= nums[m]' to handle the left-sorted side correctly.
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m-1
                else:
                    l = m+ 1
            else:
                if nums[m] < target <= nums[r]:
                    l = m+1
                else:
                    r = m-1
            
        return -1


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna