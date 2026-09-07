class Solution(object):
    def winningPlayer(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: str
        """
        ans = "Bob"
        while x >= 1 and y >= 4:
            x -= 1
            y -= 4
            if ans == "Bob":
                ans = "Alice"
            elif ans == "Alice":
                ans = "Bob"
        
        return ans