class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        x = 0
        zeros = 0
        for i in range(len(nums)):
            if nums[x] == 0:
                del nums[x]
                zeros += 1
            else:
                x += 1
        
        nums += [0] * zeros

        return nums