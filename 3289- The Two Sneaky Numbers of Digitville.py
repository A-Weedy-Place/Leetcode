class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = sorted(nums)
        ans = []
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                ans.append(nums[i])
        return ans