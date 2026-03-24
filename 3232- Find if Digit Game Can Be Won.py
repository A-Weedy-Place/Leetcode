class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a,b = 0,0
        for i in nums:
            if i >= 10:
                b += i
            else:
                a += i
        if a != b:
            return True
        else:
            return False