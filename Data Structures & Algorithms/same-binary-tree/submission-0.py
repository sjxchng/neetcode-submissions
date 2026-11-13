# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if both nodes are null -> same
        if not p and not q:
            return True
        # if one node is null -> not same
        if not p or not q:
            return False
        
        # main logic
        if p.val != q.val:
            return False
        # if same value -> check if children are also same
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)