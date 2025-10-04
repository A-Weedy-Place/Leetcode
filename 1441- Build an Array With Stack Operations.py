class Solution(object):
    def buildArray(self, target, n):
        result = []
        i = 0
        
        for num in range(1, n+1):
            if i == len(target):
                break 
            if num == target[i]:
                result.append("Push")
                i += 1
            else:
                result.append("Push")
                result.append("Pop")
        return result



class Solution(object):
    def buildArray(self, target, n):
        result = []
        prev = 0
        
        for t in target:
            for i in range(prev+1, t+1):
                result.append("Push")
                if i != t:
                    result.append("Pop")
            prev = t  
        return result