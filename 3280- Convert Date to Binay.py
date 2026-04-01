class Solution(object):
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        return str(bin(int(date[:4]))[2:]) + '-' + str(bin(int(date[5:7]))[2:]) + '-' + str(bin(int(date[8:]))[2:])