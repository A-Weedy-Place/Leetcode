class Solution(object):
    def addStrings(self, num1, num2):

        num1 = num1[::-1]
        num2 = num2[::-1]

        i = 0
        carry = 0
        res = ''

        while i < len(num1) or i < len(num2):
            if i < len(num1):
                n1 = int(num1[i])
            else:
                n1 = 0

            if i < len(num2):
                n2 = int(num2[i])
            else:
                n2 = 0

            add = n1 + n2 + carry

            if add >= 10:
                carry = 1
                add = add % 10
            else:
                carry = 0

            res += str(add)
            i += 1

        if carry:
            res += '1'

        return res[::-1]