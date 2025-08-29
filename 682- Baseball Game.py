class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        ops = []
        for i in range(len(operations)):
            if operations[i] == "+":
                ops.append(ops[-1]+ops[-2])
            elif operations[i] == "D":
                ops.append(ops[-1]*2)
            elif operations[i] == "C":
                ops.pop()
            else:
                ops.append(int(operations[i]))
        return sum(ops)
#Baseball huh?
#That tracks