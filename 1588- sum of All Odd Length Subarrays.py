class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        ans = 0
        n = len(arr)

        for i in range(n):
            s = 0
            for j in range(i, n):
                s += arr[j]
                if (j - i + 1) % 2 == 1:
                    ans += s

        return ans