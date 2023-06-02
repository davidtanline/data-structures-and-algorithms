'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''

from typing import Optional

# Given TreeNode class

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth(root: Optional[TreeNode]):
    return max(max_depth(root.left), max_depth(root.right)) + 1 if root else 0


# Construct the binary trees using TreeNode instances
tree1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
tree2 = TreeNode(1, None, TreeNode(2))

# Tests
print("Case 1 --- Expected: 3, Actual:", max_depth(tree1))
print("Case 2 --- Expected: 2, Actual:", max_depth(tree2))