class Solution(object):
    def maximizeSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        x = 0
        for i in range(k):
            x += i
        return (max(nums) * k) + x