class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        if coordinates[0] == 'a' or coordinates[0] == 'c' or coordinates[0] == 'e' or coordinates[0] == 'g':
            if int(coordinates[1])%2 == 0:
                return True
            else:
                return False
        else:
            if int(coordinates[1])%2 == 0:
                return False
            else:
                return True