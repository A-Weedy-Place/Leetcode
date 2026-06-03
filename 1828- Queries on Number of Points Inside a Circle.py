class Solution(object):
    def countPoints(self, points, queries):
        """
        :type points: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        x = []
        for i in range(len(queries)):
            x.append(0)
            for j in points:
                if ((queries[i][0]-j[0])**2 + (queries[i][1]-j[1])**2)**(0.5) <= queries[i][2]:
                    x[i] += 1
        
        return x