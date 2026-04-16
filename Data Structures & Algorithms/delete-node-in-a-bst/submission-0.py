# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.left and root.right:
                minValue = self.rootMinValue(root.right)
                root.val = minValue
                root.right = self.deleteNode(root.right, minValue)
            elif root.left:
                root = root.left
            elif root.right:
                root = root.right
                
            else:
                return None

        return root


    def rootMinValue(self, root):
        curr = root
        while curr.left:
            curr = curr.left
        return curr.val