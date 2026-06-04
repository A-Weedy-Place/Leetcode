class Solution(object):
    def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        a = 0
        for i in range(num1, num2+1):
            if i > 100:
                x = str(i)
                for j in range(1,len(x)-1):
                    if int(x[j]) > int(x[j-1]) and int(x[j]) > int(x[j+1]):
                        a += 1
                    elif int(x[j]) < int(x[j-1]) and int(x[j]) < int(x[j+1]):
                        a += 1
        return a