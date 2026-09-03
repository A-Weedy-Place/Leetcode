class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        x = ''.join(map(str, digits))
        num = int(x) + 1

        x = str(num)
        digits = list(map(int, x))

        return digits