'''
Given a binary tree, determine if it is height-balanced.
'''

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(self, root: Optional[TreeNode]) -> bool:
    if not root:
        return True

    left = self.isBalanced(root.left)
    right = self.isBalanced(root.right)

    def depth(root:Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(depth(root.left), depth(root.right))

    return left and right and abs(depth(root.left) - depth(root.right)) <= 1