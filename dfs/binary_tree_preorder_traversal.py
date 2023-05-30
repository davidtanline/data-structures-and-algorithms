'''
Given the root of a binary tree, return the preorder traversal of its nodes' values.
'''

from typing import Optional

# Given TreeNode class

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binary_tree_preorder_traversal(root: Optional[TreeNode]):
    curr, stack = root, []
    ans = []
    while curr or stack:
        if curr:
            ans.append(curr.val)
            stack.append(curr.right)
            curr = curr.left
        else:
            curr = stack.pop()
    return ans

# Construct the binary trees using TreeNode instances
tree1 = TreeNode(1, None, TreeNode(2, TreeNode(3)))
tree2 = None  # Represents an empty tree
tree3 = TreeNode(1)

# Tests
print("Case 1 --- Expected: [1, 2, 3], Actual:", binary_tree_preorder_traversal(tree1))
print("Case 2 --- Expected: [], Actual:", binary_tree_preorder_traversal(tree2))
print("Case 3 --- Expected: [1], Actual:", binary_tree_preorder_traversal(tree3))