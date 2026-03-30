class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = []
        for i in s:
            a.append(int(i))
        a.sort(reverse=True)
        del a[0]
        a.append(1)

        x = ''.join(map(str, a))
        return x
    
# Lmao i think i did it in the most retarded way possible 

        #ones = s.count('1')
        #zeroes = s.count('0')

        #ones -= 1

        #return '1' * ones + '0' * zeroes + '1'