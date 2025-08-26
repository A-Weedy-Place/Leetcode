class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        a=b=0
        for n in nums1:
            if n in nums2:
                a += 1
        for n in nums2:
            if n in nums1:
                b += 1
        return [a,b]