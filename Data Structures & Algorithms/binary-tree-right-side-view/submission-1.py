# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque()
        q.append(root)

        while q:
            right = None
            for i in range(len(q)):
                curr = q.popleft()
                if not curr:
                    continue

                right = curr.val
                q.append(curr.left)
                q.append(curr.right)
            if right:
                res.append(right)
        
        return res