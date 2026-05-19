class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        ans = 0
        for i in words:
            x = 1
            for j in i:
                if j not in allowed:
                    x = 0
                    break
            if x == 1:
                ans += 1
        return ans