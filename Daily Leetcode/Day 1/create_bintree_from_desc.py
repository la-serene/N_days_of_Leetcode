# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        children_set = []
        children_hashmap = {}

        for parent, child, isLeft in descriptions:
            if children_hashmap.get(parent, -1) == -1:
                children_hashmap[parent] = TreeNode(parent)

            if isLeft == 1:
                children_hashmap[parent].left = child
            else:
                children_hashmap[parent].right = child

            if child not in children_set:
                children_set.append(child)

        for parent, child, isLeft in descriptions:
            if parent not in children_set:
                return children_hashmap[parent]


s = Solution()
m = s.createBinaryTree([[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]])
print(m)
