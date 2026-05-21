class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):

        prefixes = set()

        # store all prefixes from arr1
        for num in arr1:
            s = str(num)
            temp = ""
            for ch in s:
                temp += ch
                prefixes.add(temp)

        ans = 0

        # check prefixes from arr2
        for num in arr2:
            s = str(num)
            temp = ""
            for ch in s:
                temp += ch
                if temp in prefixes:
                    ans = max(ans, len(temp))

        return ans