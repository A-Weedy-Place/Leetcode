class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num = []
        num.append(nums[0])
        for i in range(1,len(nums)):
            num.append(nums[i] + num[i-1])
        return num