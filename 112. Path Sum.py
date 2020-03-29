# 112. Path Sum
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that
# adding up all the values along the path equals the given sum.

# Note: A leaf is a node with no children.

# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

# Runtime: 32 ms, faster than 72.74% of Python online submissions for Path Sum.
# Memory Usage: 16.3 MB, less than 6.82% of Python online submissions for Path Sum.

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
        if root.left is None and root.right is None and root.val == sum:
            return True
        if root.left is None and root.right is None and root.val != sum:
            return False
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)


        # Shorter Solution
        if root is None:
            return False
        if not root.left and not root.right:
            return root.val == sum
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)