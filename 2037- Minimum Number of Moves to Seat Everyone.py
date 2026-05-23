class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        seats = sorted(seats)
        students = sorted(students)
        x = 0

        for i in range(len(seats)):
            x += abs(seats[i] - students[i])
        
        return x