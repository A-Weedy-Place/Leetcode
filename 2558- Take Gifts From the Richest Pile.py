import math
class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        for i in range(k):
            gifts.sort()
            gifts[-1] = int(math.sqrt(gifts[-1]))
        
        return sum(gifts)