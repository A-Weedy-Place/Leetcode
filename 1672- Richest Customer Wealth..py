class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        y = 0
        for i in range(len(accounts)):
            x = 0
            for j in range(len(accounts[0])):
                x += accounts[i][j]
            if x >= y:
                y = x
        return y