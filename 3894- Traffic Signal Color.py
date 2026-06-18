class Solution(object):
    def trafficSignal(self, timer):
        """
        :type timer: int
        :rtype: str
        """
        if timer <= 90:
            if timer > 30:
                return "Red"
            elif timer == 30:
                return "Orange"
            elif timer == 0:
                return "Green"
            else:
                return "Invalid"
        else:
            return "Invalid"   