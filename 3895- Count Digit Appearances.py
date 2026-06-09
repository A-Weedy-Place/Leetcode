class Solution(object):
    def countDigitOccurrences(self, nums, digit):
        """
        :type nums: List[int]
        :type digit: int
        :rtype: int
        """
        x = 0

        for i in nums:
            y = str(i)
            x += y.count(str(digit))
        
        return x