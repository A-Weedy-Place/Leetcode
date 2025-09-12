class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        a = []
        b = []
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))

        for n in nums1:
            if n not in nums2:
                a.append(n)
        for n in nums2:
            if n not in nums1:
                b.append(n)

        return a,b