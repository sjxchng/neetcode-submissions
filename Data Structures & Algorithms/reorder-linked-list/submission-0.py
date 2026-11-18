# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        # get the end of first half (slow)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        # after saving second (start of second half), separate first and second
        slow.next = None

        # reverse second half of linked list
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # combine
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2




