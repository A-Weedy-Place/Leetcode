class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        last = -1
        for i in range(len(num)-1,-1,-1):
            if int(num[i]) % 2 != 0:
                last = i
                break
        if last == -1:
            return ""
        else:
            return num[:i+1]