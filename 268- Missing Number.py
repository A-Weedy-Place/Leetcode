class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = len(nums)
        nums = sorted(nums)
        if nums[0] != 0:
            return 0
        if nums[-1] != a:
            return a
        for i in range(a-1):
            if nums[i] + 1 != nums [i+1]:
                return nums[i] + 1

# i am dumb. could have just summed and subtracted from expected sum