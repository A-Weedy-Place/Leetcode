class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        #EXCEEDS TIME LIMIT
        #n = len(temperatures)
        #x = []
        #while len(temperatures) != 0:
        #    z = 1
        #    if temperatures[0] == max(temperatures):
        #        x.append(0)
        #    else:
        #       for i in range(1, n):
        #            if temperatures[i] <= temperatures[0]:
        #                z += 1
        #            else:
        #                x.append(z)
        #                break
        #    del temperatures[0]
        #return x


        # ALSO EXCEEDS TIME LIMIT
        #n = len(temperatures)
        #x = [0] * n  
        #for i in range(n):
        #    z = 0
        #    for j in range(i + 1, n):
        #        if temperatures[j] > temperatures[i]:
        #            z = j - i
        #            break
        #    x[i] = z
        #return x


        n = len(temperatures)
        x = [0] * n  
        stack = []   
        for i in range(n):
            # while current temperature is greater than the top of the stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                x[prev_index] = i - prev_index  # days waited
            stack.append(i)
        return x      