class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        ans = numBottles
        empty = numBottles

        while empty >= numExchange:
            newBottles = empty // numExchange
            ans += newBottles
            empty = newBottles + (empty % numExchange)

        return ans