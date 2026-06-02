class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        x = []
        for i in range(len(strs[0])):
            for j in range(len(strs)-1):
                if ord(strs[j][i]) > ord(strs[j+1][i]):
                    x.append(i)
                    break
        
        return len(x)