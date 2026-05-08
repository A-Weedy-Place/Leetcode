class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ans = ''
        while num != 0:
            if num >= 1000:
                ans += "M"
                num -= 1000
                continue
            elif num >= 900:
                ans += "CM"
                num -= 900
                continue
            elif num >= 500:
                ans += "D"
                num -= 500
                continue
            elif num >= 400:
                ans += "CD"
                num -= 400
                continue
            elif num >= 100:
                ans += "C"
                num -= 100
                continue
            elif num >= 90:
                ans += "XC"
                num -= 90
                continue
            elif num >= 50:
                ans += "L"
                num -= 50
                continue
            elif num >= 40:
                ans += "XL"
                num -= 40
                continue
            elif num >= 10:
                ans += "X"
                num -= 10
                continue
            elif num >= 9:
                ans += "IX"
                num -= 9
                continue
            elif num >= 5:
                ans += "V"
                num -= 5
                continue
            elif num >= 4:
                ans += "IV"
                num -= 4
                continue
            elif num >= 1:
                ans += "I"
                num -= 1
                continue
        
        return ans

#this looks retarded xD.
#I need to properly learn Hashmaps. Would have made it look better tho runtime would have been the same