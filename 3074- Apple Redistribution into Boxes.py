class Solution(object):
    def minimumBoxes(self, apple, capacity):
        """
        :type apple: List[int]
        :type capacity: List[int]
        :rtype: int
        """
        capacity.sort(reverse=True)
        x = sum(apple)

        for i in range(len(capacity)):
            x -= capacity[i]
            if x <= 0:
                return i+1