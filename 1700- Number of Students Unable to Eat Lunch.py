class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        x = len(students)
        while x != 0:
            if students[0] == sandwiches[0]:
                del students[0]
                del sandwiches[0]
                x = len(students)
            else:
                students.append(students[0])
                del students[0]
                x -= 1
        
        return len(students)