class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = sorted(nums)
        ans = []

        i = 0
        for n in range(nums[0], nums[-1] + 1):
            if nums[i] != n:
                ans.append(n)
            else:
                i += 1

        return ans