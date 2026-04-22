class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        x = 0
        if len(arr) < 3:
            return False
        if arr[1] < arr [0]:
            return False
        for i in range(1,len(arr)):
            if arr[i] > arr[i-1] and x == 0:
                continue
            elif arr[i] < arr[i-1] and x == 1:
                continue
            elif arr[i] < arr[i-1] and x == 0:
                x += 1
                continue
            return False
        if x == 0:
            return False
        return True