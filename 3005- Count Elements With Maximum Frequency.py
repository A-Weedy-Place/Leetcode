class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = list(set(nums))
        maximum = 0
        a = 0

        for i in n:
            x = nums.count(i)
            if x > maximum:
                maximum = x

        for i in n:
            if nums.count(i) == maximum:
                a += 1

        return a * maximum