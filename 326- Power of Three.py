class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n >= 3:
            n /= 3.0
        if n == 1:
            return True
        else:
            return False

#this recurrusing loop is nice:
#def isPowerOfThree(self, n):
#        if n==1:
#            return True
#        if n<=0:
#            return False
#        if n%3!=0:
#            return False
#            
#        return self.isPowerOfThree(n//3)   