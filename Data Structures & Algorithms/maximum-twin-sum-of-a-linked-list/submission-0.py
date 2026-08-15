# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        res = 0
        values = {}
        index = -1

        while fast and fast.next:
            index += 1
            values[str(index)] = slow.val
            slow = slow.next
            fast = fast.next.next


        while slow:
            res = max(res, values[str(index)] + slow.val)
            slow = slow.next
            index -= 1

        return res