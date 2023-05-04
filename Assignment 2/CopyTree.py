'''
Ahmed Hashim
Time 38 mins
Technique: Breadth-first search

Time Complexity: O(n)
Space Complexity: O(n)


'''


def CopyTree(root):
    if not root:
        return None
    else:
        stack = [(root, None)]
        copy = Node(root.val)
        copies = {root: copy}
        while stack:
            node, parent_copy = stack.pop()
            if node.left:
                left_copy = Node(node.left.val)
                copies[node.left] = left_copy
                copies[node].left = left_copy
                stack.append((node.left, node))
            if node.right:
                right_copy = Node(node.right.val)
                copies[node.right] = right_copy
                copies[node].right = right_copy
                stack.append((node.right, node))
        return copy
