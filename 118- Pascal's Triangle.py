class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        a = []
        for x in range(1, numRows+1):
            b = [1] * x
            if x>2:
                for y in range(1, x-1):
                    b[y] = a[x-2][y-1] + a[x-2][y]
            a.append(b)
        return a