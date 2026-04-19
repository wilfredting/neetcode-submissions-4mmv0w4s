# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []
        stack = []
        curr = root

        while (curr or values) and len(values) < k:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            values.append(curr.val)
            curr = curr.right

        return values[k-1]