class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = ''
        digit = 0
        for i in nums:
            s = str(i)
            for j in range(len(s)):
                digit += int(s[j])
        return abs(sum(nums) - digit)