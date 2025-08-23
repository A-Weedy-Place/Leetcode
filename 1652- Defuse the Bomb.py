class Solution(object):
    def decrypt(self, code, k):
        n = len(code)
        res = [0] * n   # result array

        if k == 0:
            return res

        for i in range(n):
            if k > 0:
                # sum of next k numbers
                for j in range(1, k+1):
                    res[i] += code[(i + j) % n]
            else:
                # sum of previous |k| numbers
                for j in range(1, -k+1):
                    res[i] += code[(i - j) % n]

        return res