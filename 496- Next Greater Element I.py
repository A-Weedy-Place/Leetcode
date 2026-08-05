class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        ans = []

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums2[j] == nums1[i]:
                    found = False

                    for k in range(j + 1, len(nums2)):
                        if nums2[k] > nums2[j]:
                            ans.append(nums2[k])
                            found = True
                            break

                    if not found:
                        ans.append(-1)

                    break

        return ans  