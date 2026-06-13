class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) > 1:
            while len(nums) != 1:
                for i in range(len(nums)-1):
                    nums[i] = (nums[i] + nums[i+1]) % 10
                del nums[-1]
        return nums[0]