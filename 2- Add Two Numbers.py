# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        uwu = ListNode(0)
        current = uwu

        carry = 0
        while l1 != None or l2 != None or carry:
            add = carry

            if l1 != None:
                add += l1.val
                l1 = l1.next

            if l2 != None:
                add += l2.val
                l2 = l2.next

            if add > 9:
                carry = 1
                add %= 10
            else:
                carry = 0

            current.next = ListNode(add)
            current = current.next
        
        return uwu.next