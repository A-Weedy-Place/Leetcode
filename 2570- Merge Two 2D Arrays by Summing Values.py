class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        a, b = 0, 0
        ans = []

        while a < len(nums1) and b < len(nums2):
            if nums1[a][0] == nums2[b][0]:
                ans.append([nums1[a][0], nums1[a][1] + nums2[b][1]])
                a += 1
                b += 1
            elif nums1[a][0] < nums2[b][0]:
                ans.append(nums1[a])
                a += 1
            else:
                ans.append(nums2[b])
                b += 1

        while a < len(nums1):
            ans.append(nums1[a])
            a += 1

        while b < len(nums2):
            ans.append(nums2[b])
            b += 1

        return ans