class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = len(nums)
        for i in range(a + 1):
            n = 0
            for num in nums:
                if num >= i:
                    n += 1
            if n == i:
                return i
        return -1