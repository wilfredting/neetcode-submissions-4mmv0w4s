# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr and curr.next:
            tmp = curr
            curr = curr.next
            tmp.next = prev
            prev = tmp
        if curr:
            curr.next = prev

        return curr