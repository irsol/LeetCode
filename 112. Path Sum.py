# 112. Path Sum
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that
# adding up all the values along the path equals the given sum.

# Note: A leaf is a node with no children.

# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        # Return False if root is empty 
        if root is None:
            return False 
