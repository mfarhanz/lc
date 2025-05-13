# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        # basically merge sort adapted for linked list instead of array
        i = 0
        tmp = head
        left, right = ListNode(), ListNode()
        curr_l, curr_r = left, right
        # get count of elements
        while tmp:
            tmp = tmp.next
            i += 1
        # get left half
        for _ in range(i//2):
            curr_l.next = ListNode(head.val)
            curr_l = curr_l.next
            head = head.next
        # get right half
        for _ in range(i//2, i):
            curr_r.next = ListNode(head.val)
            curr_r = curr_r.next
            head = head.next
        return self.merge(self.sortList(left.next), self.sortList(right.next))
    
    def merge(self, left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
        # standard merge function adapted for linked list
        res = ListNode()
        curr = res
        while left and right:
            if left.val < right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        if left:
            curr.next = left
        if right:
            curr.next = right
        return res.next
