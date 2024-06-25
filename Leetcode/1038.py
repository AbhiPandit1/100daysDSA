"""
Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
Example 2:

Input: root = [0,null,1]
Output: [1,null,1]
    
"""

"""
First way create a function normal
array [add all the value with index]
then create another array and add corresponding value sum of greater then them and then assign the index to it 

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def copy_tree(node):
            if not node:
                return None
            new_node = TreeNode(node.val)
            new_node.left = copy_tree(node.left)
            new_node.right = copy_tree(node.right)
            return new_node

        def reverse_in_order(node):
            if not node:
                return
            reverse_in_order(node.right)
            self.sum += node.val
            node.val = self.sum
            reverse_in_order(node.left)

        new_root = copy_tree(root)
        self.sum = 0
        reverse_in_order(new_root)
        return new_root
