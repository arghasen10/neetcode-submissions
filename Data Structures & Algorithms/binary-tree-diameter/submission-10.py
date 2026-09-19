# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def heightOfTree(root):
    if not root:
        return 0
    # if (root.left is None) and (root.right is None):
    #     return 0
    return 1 + max(heightOfTree(root.left), heightOfTree(root.right))
class Solution:
    def __init__(self):
        self.max = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        lefttree = heightOfTree(root.left)
        righttree = heightOfTree(root.right)
        diameter = lefttree+righttree
        sub = self.diameterOfBinaryTree(root.left)+self.diameterOfBinaryTree(root.right)
        return max(diameter, sub)
        # if root.left is None and root.right is None:
        #     return 0
        # elif root.left is None:
        #     return 1 + heightOfTree(root.right)
        # elif root.right is None:
        #     return 1 + heightOfTree(root.left)    
        # else:
        #     self.max = max (self.max, 2 + heightOfTree(root.left) + heightOfTree(root.right)) 
        #     print(self.max)
        #     return self.max
        