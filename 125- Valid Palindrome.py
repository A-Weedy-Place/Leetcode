class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(c for c in s if c.isalnum())
        s = s.lower()
        L = 0
        R = len(s)-1
        while L <= R:
            if s[L] == s[R]:
                L += 1
                R -= 1
            else:
                return False
        return True