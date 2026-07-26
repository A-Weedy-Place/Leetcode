class Solution(object):
    def mapWordWeights(self, words, weights):
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        ans = ''
        for i in words:
            x = 0
            for j in i:
                x += weights[ord(j)-97]
            x %= 26
            ans += chr(122-x)
        
        return ans