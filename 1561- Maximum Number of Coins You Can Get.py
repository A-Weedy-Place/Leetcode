class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        x = 0

        # memory 100%
        # while piles != []:
        #     x += piles[-2]
        #     piles.pop(0)
        #     piles.pop(-1)
        #     piles.pop(-1)
        # return x

        #runtime good
        for i in range((len(piles)/3),len(piles),2):
            x += piles[i]
        return x

# My sol was basically this:
# I just like how concise it is
        # piles.sort()
        # n = len(piles) // 3
        # return sum(piles[n::2])