# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # DFS
        # the current node's depth is 1+max(left,right)
        # recursion
        # if not root:
        #     return 0
        # return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
        # BFS
        # give a deque, everytime when you go one depth lower, treverse all the nodes for the next layer, until the next layer is all null
        if not root:
            return 0
        depth = 0
        q=deque()
        q.append(root)
        while q:
            depth +=1
            for _ in range(len(q)): # execute just once, even the q is later appended with more nodes
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return depth


