'''
Given the root of a binary tree, return the inorder traversal of its nodes' values.
'''

from typing import Optional

# Given TreeNode class

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binary_tree_inorder_traversal(root: Optional[TreeNode]):
    curr, stack = root, []
    ans = []
    while curr or stack:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            ans.append(curr.val)
            curr = curr.right
    return ans

# Construct the binary trees using TreeNode instances
tree1 = TreeNode(1, None, TreeNode(2, TreeNode(3)))
tree2 = None  # Represents an empty tree
tree3 = TreeNode(1)

# Tests
print("Case 1 --- Expected: [1, 3, 2], Actual:", binary_tree_inorder_traversal(tree1))
print("Case 2 --- Expected: [], Actual:", binary_tree_inorder_traversal(tree2))
print("Case 3 --- Expected: [1], Actual:", binary_tree_inorder_traversal(tree3))