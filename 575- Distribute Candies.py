class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        n = len(candyType)/2
        candyType = len(list(set(candyType)))

        if (candyType <= n):
            return candyType
        else:
            return n
        
# or a 1 line sol but same thing
#return min(len(set(candyType)), len(candyType) // 2)