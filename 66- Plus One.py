class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = [0] + digits
        for i in range(len(digits)-1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                break
            else:
                digits[i] = 0
        if digits[0] == 0:
            del digits[0]
        return digits