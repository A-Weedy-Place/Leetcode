        #Exceeds time limit
        #ans = []
        #a = [0,0,0]
        #for i in range(len(nums)):
        #    a[0] = nums[i]
        #    for j in range(i+1,len(nums)):
        #        a[1] = nums[j]
        #        for k in range(j+1,len(nums)):
        #            a[2] = nums[k]
        #            if sum(a) == 0:
        #                ans.append(tuple(sorted(a)))
        #x = list(set(ans))
        #return [list(i) for i in x]

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def twoSum(arr, target):
            seen = {}
            pairs = []
            for i, num in enumerate(arr):
                diff = target - num
                if diff in seen:
                    pairs.append((diff, num))
                seen[num] = i
            return pairs 

        ans = set() 

        for i in range(len(nums)):
            target = -nums[i]
            pairs = twoSum(nums[i + 1:], target)

            for (x, y) in pairs:
                triplet = tuple(sorted((nums[i], x, y)))
                ans.add(triplet)

        return [list(t) for t in ans]
