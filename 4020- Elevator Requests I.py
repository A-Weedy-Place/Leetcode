class Solution(object):
    def elevatorRequests(self, n, requests):
        """
        :type n: int
        :type requests: List[int]
        :rtype: int
        """
        ans = 0
        x = 0
        for i in requests:
            x = abs(x-i)
            ans += x
            x = i

        return ans    