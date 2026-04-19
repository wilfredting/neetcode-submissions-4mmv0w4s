# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        def inorder(arr, root):
            if not root:
                return None
            inorder(arr, root.left)
            arr.append(root.val)
            inorder(arr, root.right)

        inorder(res, root)
        return res