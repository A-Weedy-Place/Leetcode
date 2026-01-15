class Solution(object):
    def finalPositionOfSnake(self, n, commands):
        """
        :type n: int
        :type commands: List[str]
        :rtype: int
        """
        val = 0
        for i in commands:
            if i == "RIGHT":
                val += 1
            elif i == "LEFT":
                val -= 1
            elif i == "UP":
                val -= n
            elif i == "DOWN":
                val += n
        return val