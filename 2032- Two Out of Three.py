class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        ans = []
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        nums3 = list(set(nums3))

        for i in range(len(nums1)):
            if nums1[i] in nums2:
                ans.append(nums1[i])
            elif nums1[i] in nums3:
                ans.append(nums1[i])
        
        for i in range(len(nums2)):
            if nums2[i] in nums3:
                ans.append(nums2[i])

        return list(set(ans))