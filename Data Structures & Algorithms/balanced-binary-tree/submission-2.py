# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import numpy as np
class Solution:
    def heightofTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.heightofTree(root.left), self.heightofTree(root.right))
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if np.abs(self.heightofTree(root.left) - self.heightofTree(root.right))>1:
            return False
        # if self.heightofTree(root.left) >= self.heightofTree(root.right):
        #     return root
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        