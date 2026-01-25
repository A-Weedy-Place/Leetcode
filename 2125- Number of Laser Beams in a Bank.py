class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        a=[]
        count = 0
        for i in bank:
            counter = 0
            for j in i:
                if j == '1':
                    counter += 1
            if counter > 0:
                a.append(counter)
        for i in range(len(a)-1):
            count += a[i] * a[i+1]
        return count 