class Solution(object):
    def isWinner(self, player1, player2):
        """
        :type player1: List[int]
        :type player2: List[int]
        :rtype: int
        """ 
        r1 = r2 = 0
        for i in range(len(player1)):
            
            if (i >= 1 and player1[i-1] == 10) or (i >= 2 and player1[i-2] == 10):
                r1 += 2 * player1[i]
            else:
                r1 += player1[i]
            if (i >= 1 and player2[i-1] == 10) or (i >= 2 and player2[i-2] == 10):
                r2 += 2 * player2[i]
            else:
                r2 += player2[i]

        if r1 > r2:
            return 1
        elif r2 > r1:
            return 2
        else:
            return 0