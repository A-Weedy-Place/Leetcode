class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        x = [0]
        for i in range(len(s)):
            #if s[i] == "(" or s[i] == "{" or s[i] == "[":
            #    x.append(s[i])
            x.append(s[i])
            if s[i] == ")":
                if x[-2] == "(":
                    x.pop()
                    x.pop()
            elif s[i] == "}":
                if x[-2] == "{":
                    x.pop()
                    x.pop()
            elif s[i] == "]":
                if x[-2] == "[":
                    x.pop()
                    x.pop()
        if x == [0]:
            return True
        else:
            return False