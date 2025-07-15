class Solution(object):
    
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        a = max(candies)
        for x in range(len(candies)):
            candies[x] += extraCandies
            if candies[x] >= a:
                candies[x] = True
            else:
                candies[x] = False
        return candies