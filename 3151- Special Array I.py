class Solution(object):
    def isArraySpecial(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        x = 2
        for i in range(len(nums)-1):
            if nums[i] % 2 == 0:
                if nums[i+1] % 2 != 1:
                    return False
            else:
                if nums[i+1] % 2 != 0:
                    return False
        
        return True