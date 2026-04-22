# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def dfs(preorder, inorder):
            if not preorder or not inorder:
                return

            val = preorder[0]
            curr = TreeNode(val)
            index = inorder.index(val)
            left_inorder = inorder[:index]
            right_inorder = inorder[index + 1:]
            left_preorder = preorder[1:len(left_inorder) + 1]
            right_preorder = preorder[len(left_inorder) + 1:]
            curr.left = dfs(left_preorder, left_inorder)
            curr.right = dfs(right_preorder, right_inorder)

            return curr



        return dfs(preorder, inorder)
