class Solution(object):
    def earliestTime(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: int
        """
        s = tasks[0][0] + tasks[0][1]
        for i in range(1,len(tasks)):
            if tasks[i][0] + tasks[i][1] < s:
                s = tasks[i][0] + tasks[i][1]
        return s