class Solution(object):
    def canReach(self, start, target):
        """
        :type start: List[int]
        :type target: List[int]
        :rtype: bool
        """
        if (start[0] + start[1]) % 2 == 0:
            if (target[0] + target[1]) % 2 == 0:
                return True
            else:
                return False
        else:
            if (target[0] + target[1]) % 2 == 1:
                return True
            else:
                return False