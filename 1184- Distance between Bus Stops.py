class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        a = sum(distance)
        dist = 0

        if destination < start:
            start, destination = destination, start

        for i in range(start, destination):
            dist += distance[i]

        a = a - dist

        if dist <= a :
            return dist
        else:
            return a