class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        n = str(num)
        count = 0
        for i in n:
            if num % int(i) == 0:
                count += 1
        return count