class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(len(nums)):
            if nums[i] not in nums[0:i] and nums[i] not in nums[i+1:len(nums)]:
                ans += nums[i]
        return ans