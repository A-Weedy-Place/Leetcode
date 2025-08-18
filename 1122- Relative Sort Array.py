class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        x = []
        for i in arr2:
            while i in arr1:
                x.append(i)
                arr1.remove(i)
        arr1.sort()
        return x + arr1