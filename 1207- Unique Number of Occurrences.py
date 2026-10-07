class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        x = list(set(arr))
        a = []
        for i in x:
            a.append(arr.count(i))

        if len(x) == len(set(a)):
            return True
        else:
            return False  