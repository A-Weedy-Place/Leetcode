class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        a = len(nums)
        i = 0
        b = nums.count(2)
        a -= b
        while i != a:
            if nums[i] == 2:
                del nums[i]
                nums.append(2)
            elif nums[i] == 0:
                del nums[i]
                nums.insert(0,0)
                i += 1
            else:
                i += 1
        return nums