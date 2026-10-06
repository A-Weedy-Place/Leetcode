class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(1,len(nums)):
            x = 0
            if nums[i] <= nums[i-1]:
                x = nums[i-1] - nums[i] + 1
                nums[i] += x
                ans += x
        
        return ans