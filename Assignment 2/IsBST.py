'''
Technique: Depth-first traversal
Time Complexity: O(n), where n is the number of nodes in the tree
Space Complexity: O(h), where h is the height of the tree (recursive call stack space)
Time: 45mins
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def is_bst(root):
        def dfs(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True
            if node.val <= lower or node.val >= upper:
                return False
            return dfs(node.left, lower, node.val) and dfs(node.right, node.val, upper)

        return dfs(root)

# Test Cases
"""
Example 1:
Input:
2
/
1 3
Output: True
Explanation: The tree is a valid binary search tree.

Example 2:
Input:
5
/
1 4
/
3 6
Output: False
Explanation: The root node's value is 5 but its right child's value is 4, which violates the definition of a binary search tree.
"""
root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(3)
assert is_bst(root1) == True

root2 = TreeNode(5)
root2.left = TreeNode(1)
root2.right = TreeNode(4)
root2.right.left = TreeNode(3)
root2.right.right = TreeNode(6)
assert is_bst(root2) == False
