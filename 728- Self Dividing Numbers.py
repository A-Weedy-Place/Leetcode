class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        x = 0
        ans = []
        for i in range(left, right+1):
            for j in str(i):
                if j == '0':
                    x = 0
                    break
                elif i % int(j) == 0:
                    x = 1
                else:
                    x = 0
                    break
            if x == 1:
                ans.append(i)
        return ans  