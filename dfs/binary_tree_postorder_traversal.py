'''
Given the root of a binary tree, return the postorder traversal of its nodes' values.
'''

from typing import Optional

# Given TreeNode class

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binary_tree_postorder_traversal(root: Optional[TreeNode]):
    stack = [root]
    visit = [False]
    ans = []

    while stack:
        curr, v = stack.pop(), visit.pop()
        if curr:
            if v:
                ans.append(curr.val)
            else:
                stack.append(curr)
                visit.append(True)
                stack.append(curr.right)
                visit.append(False)
                stack.append(curr.left)
                visit.append(False)
    return ans

# Construct the binary trees using TreeNode instances
tree1 = TreeNode(1, None, TreeNode(2, TreeNode(3)))
tree2 = None  # Represents an empty tree
tree3 = TreeNode(1)

# Tests
print("Case 1 --- Expected: [3, 2, 1], Actual:", binary_tree_postorder_traversal(tree1))
print("Case 2 --- Expected: [], Actual:", binary_tree_postorder_traversal(tree2))
print("Case 3 --- Expected: [1], Actual:", binary_tree_postorder_traversal(tree3))