class Solution(object):
    def findDelayedArrivalTime(self, arrivalTime, delayedTime):
        """
        :type arrivalTime: int
        :type delayedTime: int
        :rtype: int
        """
        ans = arrivalTime + delayedTime
        if ans > 23:
            return ans % 24
        return ans