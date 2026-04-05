class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = 0
        for i in nums:
            i = len(str(i))
            if i%2 == 0:
                x += 1
        return x