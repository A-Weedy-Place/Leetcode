class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        x=0
        for i in items:
            if ruleKey == "type":
                if i[0] == ruleValue:
                    x+=1
            elif ruleKey == "color":
                if i[1] == ruleValue:
                    x+=1
            elif ruleKey == "name":
                if i[2] == ruleValue:
                    x+=1
        return x
    