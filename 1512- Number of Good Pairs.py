class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = 0
        for i in range(len(nums)-1):
            for j in range(i,len(nums)):
                if i<j:
                    if nums[i] == nums[j]:
                        x += 1
        return x