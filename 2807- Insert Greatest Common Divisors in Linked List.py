# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        curr = head
        while curr and curr.next:                             
            new_node = ListNode(gcd(curr.val, curr.next.val))  
            t = curr.next
            curr.next = new_node
            new_node.next = t
            curr = t
        return head