class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        ans = 0
        for i in operations:
            if i == "--X" or i == "X--":
                ans -= 1
            elif i == "++X" or "X++":
                ans += 1
        return ans