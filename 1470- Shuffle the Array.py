class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        x = []
        for i in range(n):
            x.append(nums[i])
            x.append(nums[i+n])
        return x