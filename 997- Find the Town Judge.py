class Solution(object):
    def findJudge(self, n, trust):
        a = [i for i in range(1, n+1)]
        
        # remove anyone who trusts somebody
        for t in trust:
            if t[0] in a:
                a.remove(t[0])

        # check all remaining candidates
        for candidate in a:
            count = 0
            for t in trust:
                if t[1] == candidate:
                    count += 1
            if count == n - 1:
                return candidate
        
        return -1

#best sol
        # count = [0] * (n + 1)

        # for i , j in trust:
        #    count[i] -= 1
        #    count[j] += 1

        # for i in range(1 , n + 1):
        #   if count[i] == n -1:
        #     return i

        # return -1