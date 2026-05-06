class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        res = []

        while columnNumber != 0:
            rem = columnNumber % 26
            
            if rem == 0:
                res.append(26)
                columnNumber = columnNumber // 26 - 1
            else:
                res.append(rem)
                columnNumber //= 26


        res = res[::-1]

        x = ''
        for i in res:
            x += (chr(i+64))
        
        return x