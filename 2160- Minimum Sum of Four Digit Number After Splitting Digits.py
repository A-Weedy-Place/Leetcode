class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = str(num)
        a = [int(x) for x in num]
        a.sort()
        return ((a[0]*10) + a[3]) + ((a[1]*10) + a[2])