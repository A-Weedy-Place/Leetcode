class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        s = list(s)
        a = len(s)
        s.append("A")
        for z in range(a):
            if s[z] =="M":
                ans += 1000
            elif s[z] == "D":
                ans += 500
            elif s[z] == "C":
                if s[z+1] == "M" or s[z+1] == "D":
                    ans -= 100
                else:
                    ans += 100
            elif s[z] == "L":
                ans += 50
            elif s[z] == "X":
                if s[z+1] == "L" or s[z+1] == "C":
                    ans -= 10
                else:
                    ans += 10
            elif s[z] == "V":
                ans += 5
            elif s[z] == "I":
                if s[z+1] == "V" or s[z+1] == "X":
                    ans -= 1
                else:
                    ans += 1
        return ans