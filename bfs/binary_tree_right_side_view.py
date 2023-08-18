'''
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
'''

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return None
        
        res, queue = [], deque()

        queue.append(root)

        while queue:
            n = len(queue)
            for i in range(0, n):
                treeNode = queue.popleft()
                if (treeNode.left): queue.append(treeNode.left)
                if (treeNode.right): queue.append(treeNode.right)
                if i == n - 1: res.append(treeNode.val)

        return res