class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        x = [first]
        for i in encoded:
            x.append(x[-1] ^ i)
        return x