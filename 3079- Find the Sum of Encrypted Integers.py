class Solution(object):
    def sumOfEncryptedInt(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in nums:
            if i < 10:
                ans += i
            else:
                digits = list(map(int, str(i)))
                x = max(digits)
                y = len(digits)

                ans += int(str(x) * y)
        
        return ans