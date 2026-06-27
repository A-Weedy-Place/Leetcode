class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        x = 0
        for i in range(len(nums)):
            if nums[x] % 2 == 1:
                nums.append(nums[x])
                del nums[x]
            else:
                x += 1
        return nums

        #using a different list would have been easier