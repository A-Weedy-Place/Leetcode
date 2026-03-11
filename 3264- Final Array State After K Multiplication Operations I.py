class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        """
        :type nums: List[int]
        :type k: int
        :type multiplier: int
        :rtype: List[int]
        """
        for i in range(k):
            smallest = nums[0]
            small = 0
            for j in range(len(nums)):
                if nums[j] < smallest:
                    smallest = nums[j]
                    small = j
            nums[small] *= multiplier
        return nums 