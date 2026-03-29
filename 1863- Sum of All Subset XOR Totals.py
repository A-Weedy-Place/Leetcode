class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def sums(term, idx):
            if idx == len(nums):
                return term            
            return sums(term, idx + 1) + sums(term ^ nums[idx], idx + 1)
        
        return sums(0, 0)