class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        x = ''
        a = 0
        if num < 0:
            a = 1
        num = abs(num)
        while num != 0:
            if num > 6:
                x = x + str(num % 7)
                num //= 7
            else:
                x = x + (str(num % 7))
                num = 0
        if a == 0:        
            return x[::-1]
        else:
            return '-' + x[::-1] 