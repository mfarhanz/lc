# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode()
        curr_sum = l3
        d1, d2 = None, None
        while l1 is not None or l2 is not None:
            d1 = l1.val
            d2 = l2.val
            if l1.next is not None or l2.next is not None:
                curr_sum.next = ListNode()
            if d1 + d2 > 9:
                curr_sum.val += (d1 + d2) % 10
                carry = int(str(d1 + d2)[:1])
                if l1.next is not None:
                    l1.next.val += carry
                elif l2.next is not None:
                    l2.next.val += carry
                else:
                    curr_sum.next = ListNode(carry)
            else:
                curr_sum.val += d1 + d2
            if l1.next is not None and l2.next is None:
                l1 = l1.next
                l2 = ListNode()
            elif l1.next is None and l2.next is not None:
                l1 = ListNode()
                l2 = l2.next
            else:
                l1 = l1.next
                l2 = l2.next
            curr_sum = curr_sum.next
        return l3
            
            
