class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        x = 0
        for i in sentences:
            if i.count(" ") > x:
                x = i.count(" ")
        return x + 1