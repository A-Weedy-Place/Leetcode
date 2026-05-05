class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        columnTitle = columnTitle[::-1]

        x = [ord(i)-64 for i in columnTitle]
        
        a,res = 0,0
        for i in range(len(x)):
            res += x[i] * (26**a)
            a += 1
        
        return res