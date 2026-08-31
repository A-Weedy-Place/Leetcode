class Solution(object):
    def findArray(self, pref):
        """
        :type pref: List[int]
        :rtype: List[int]
        """
        if len(pref) == 1:
            return pref

        ans = [pref[0]]

        for i in range(1,len(pref)):
            ans.append(pref[i] ^ pref[i-1])
        
        return ans