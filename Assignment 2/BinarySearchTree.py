class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __repr__(self):
        return self._traverse(self.root)

    def _traverse(self, node):
        if node is None:
            return ''
        return f'{self._traverse(node.left)}{node.val}, {self._traverse(node.right)}'

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
            return

        curr = self.root
        while True:
            if val == curr.val:
                print(f"{val} is already in the tree")
                return

            if val < curr.val:
                if curr.left is None:
                    curr.left = Node(val)
                    return
                else:
                    curr = curr.left

            else:
                if curr.right is None:
                    curr.right = Node(val)
                    return
                else:
                    curr = curr.right

    def min(self):
        if self.root is None:
            return None

        curr = self.root
        while curr.left is not None:
            curr = curr.left
        return curr.val

    def max(self):
        if self.root is None:
            return None

        curr = self.root
        while curr.right is not None:
            curr = curr.right
        return curr.val

    def contains(self, val):
        curr = self.root
        while curr is not None:
            if val == curr.val:
                return True
            elif val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return False

    def delete(self, val):
        if self.root is None:
            return

        # Find the node to be deleted
        curr = self.root
        parent = None
        while curr is not None:
            if val == curr.val:
                break
            elif val < curr.val:
                parent = curr
                curr = curr.left
            else:
                parent = curr
                curr = curr.right

        if curr is None:
            print(f"{val} is not in the tree")
            return

        # Case 1: node to be deleted is a leaf node
        if curr.left is None and curr.right is None:
            if curr == self.root:
                self.root = None
            elif parent.left == curr:
                parent.left = None
            else:
                parent.right = None

        # Case 2: node to be deleted has one child
        elif curr.left is None:
            if curr == self.root:
                self.root = curr.right
            elif parent.left == curr:
                parent.left = curr.right
            else:
                parent.right = curr.right

        elif curr.right is None:
            if curr == self.root:
                self.root = curr.left
            elif parent.left == curr:
                parent.left = curr.left
            else:
                parent.right = curr.left

        # Case 3: node to be deleted has two children
        else:
            # Find the minimum value in the right subtree
            min_right = curr.right
            while min_right.left is not None:
                min_right = min_right.left

            # Copy the value of the minimum node to the node to be deleted
            curr.val = min_right.val

            # Delete the minimum node
            self.delete(min_right.val)
