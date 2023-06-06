'''
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 

This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
'''

from typing import Optional

# Given TreeNode class


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    abs_max = 0

    def diameter(self, root: Optional[TreeNode]) -> int:
        # return max of (absolute max, left+right)
        if not root:
            return 0
        return max(self.dfs(root.left) + self.dfs(root.right), self.abs_max)

    def dfs(self, root: Optional[TreeNode]):
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        self.abs_max = max(self.abs_max, left + right)
        return 1 + max(left, right)


# Construct the binary trees using TreeNode instances
tree1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
tree2 = None  # Represents an empty tree
tree3 = TreeNode(TreeNode(1), TreeNode(2))

solution = Solution()

# Tests
print("Case 1 --- Expected: 3, Actual:", solution.diameter(tree1))
print("Case 2 --- Expected: 0, Actual:", solution.diameter(tree2))
print("Case 3 --- Expected: 1, Actual:", solution.diameter(tree3))
