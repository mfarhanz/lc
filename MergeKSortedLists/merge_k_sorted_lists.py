# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        # merge() part of mergesort, but for linked-list
        i = 1
        left, right = lists[i-1], None
        while i < len(lists):
            res = ListNode()
            curr = res
            right = lists[i]
            while left and right:
                if left.val < right.val:
                    curr.next = ListNode(left.val)
                    left = left.next
                else:
                    curr.next = ListNode(right.val)
                    right = right.next
                curr = curr.next
            curr.next = left if left else right
            left = res.next
            i += 1
        return res.next
