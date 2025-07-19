class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = [0] * len(nums)
        for i in range(len(nums)):
            x=0
            for j in range(len(nums)):
                if j == i:
                    continue
                if nums[i] > nums[j]:
                    x += 1
                arr[i] = x
        return arr