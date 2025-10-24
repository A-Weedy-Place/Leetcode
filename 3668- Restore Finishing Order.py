class Solution(object):
    def recoverOrder(self, order, friends):
        """
        :type order: List[int]
        :type friends: List[int]
        :rtype: List[int]
        """
        
        fo = []
        for i in order:
            if i in friends:
                fo.append(i)
        return fo