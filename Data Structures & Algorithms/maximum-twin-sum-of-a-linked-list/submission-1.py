# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        prev = None

        while fast and fast.next:
            temp = slow
            slow = slow.next
            fast = fast.next.next
            temp.next = prev
            prev = temp

        res = 0
        while slow:
            res = max(res, slow.val + prev.val)
            slow = slow.next
            prev = prev.next

        return res