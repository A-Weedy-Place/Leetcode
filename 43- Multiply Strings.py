class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        x = []
        y = []
        for i in num1:
            x.append(ord(i)-48)
        for i in num2:
            y.append(ord(i)-48)
        
        num = 0
        for i in x:
            num = num * 10 + i
        
        a = num
        num = 0
        for i in y:
            num = num * 10 + i
        
        b = num

        return str(a*b)


        # i probably didnt what i was supposed to do lol
        # ig the ascii conversion was a fine approach but i still dont understand how