class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        digits = ['0','1','2','3','4','5','6','7','8','9']

        result = []
        for ch in s:
            if ch in digits:
                if result:
                    result.pop()
            else:
                result.append(ch)
        return ''.join(result)