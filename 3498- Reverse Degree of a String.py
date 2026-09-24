class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        for i in range(len(s)):
            ans += (abs(ord(s[i])-97-26) * (i+1))
            
        return ans