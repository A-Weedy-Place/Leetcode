class Solution(object):
    def groupThePeople(self, groupSizes):
        x = sorted(list(set(groupSizes)))
        ans = []

        for i in range(len(x)):
            k = len(ans)

            for j in range(len(groupSizes)):
                if groupSizes[j] == x[i]:

                    if len(ans) <= k:
                        ans.append([])

                    ans[k].append(j)

                    if len(ans[k]) == x[i]:
                        k += 1
        return ans