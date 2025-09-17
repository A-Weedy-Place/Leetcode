class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #b = []
        #ans = []
        #while len(nums) != 0:
        #    a.append(min(nums))
        #    nums.remove(min(nums))
        #    b.append(min(nums))
        #    nums.remove(min(nums))
        #for i in range(len(a)):
        #    ans.append(b[i])
        #    ans.append(a[i])
        #return ans


        # SOl:2 beats 100%
        nums.sort()
        ans = []
        for i in range(0, len(nums), 2):
            ans.append(nums[i+1])  
            ans.append(nums[i])    
        return ans