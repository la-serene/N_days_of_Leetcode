from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        children_set = {}
        children_hashmap = {}

        for parent, child, isLeft in descriptions:
            if children_hashmap.get(parent, -1) == -1:
                children_hashmap[parent] = TreeNode(parent)

            if children_hashmap.get(child, -1) == -1:
                children_hashmap[child] = TreeNode(child)

            if isLeft == 1:
                children_hashmap[parent].left = children_hashmap[child]
            else:
                children_hashmap[parent].right = children_hashmap[child]

            if children_set.get(child, 0) == 0:
                children_set[child] = 1

        for parent, _, _ in descriptions:
            if children_set.get(parent, 0) == 0:
                return children_hashmap[parent]


s = Solution()
m = s.createBinaryTree([[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]])
print(m)
