class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        x = []
        y = []
        z = []

        for i in range(len(nums)):
            if nums[i] < pivot:
                x.append(nums[i])
            elif nums[i] > pivot:
                y.append(nums[i])
            else:
                z.append(nums[i])
        
        return x + z + y