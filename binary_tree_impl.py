class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def add_root(self, value):
        """Add a root to the tree if it doesn't exist."""
        if self.root is None:
            self.root = Node(value)
        else:
            print("Root already exists.")

    def add_left(self, parent, value):
        """Add a left child to a given parent node."""
        if parent.left is None:
            parent.left = Node(value)
        else:
            print(f"Node {parent.value} already has a left child.")

    def add_right(self, parent, value):
        """Add a right child to a given parent node."""
        if parent.right is None:
            parent.right = Node(value)
        else:
            print(f"Node {parent.value} already has a right child.")

    def inorder_traversal(self, node):
        """Perform an inorder traversal and return the elements as a list."""
        if node is None:
            return []
        return (
            self.inorder_traversal(node.left) +
            [node.value] +
            self.inorder_traversal(node.right)
        )

    def preorder_traversal(self, node):
        """Perform a preorder traversal and return the elements as a list."""
        if node is None:
            return []
        return (
            [node.value] +
            self.preorder_traversal(node.left) +
            self.preorder_traversal(node.right)
        )

    def postorder_traversal(self, node):
        """Perform a postorder traversal and return the elements as a list."""
        if node is None:
            return []
        return (
            self.postorder_traversal(node.left) +
            self.postorder_traversal(node.right) +
            [node.value]
        )
    
    def is_bst(self, node, min_val=float('-inf'), max_val=float('inf')):
        # Base case: An empty tree is a BST
        if node is None:
            return True

        # Check if the current node's value violates the min/max constraint
        if not (min_val < node.value < max_val):
            return False

        # Recursively check the left and right subtrees with updated constraints
        return (self.is_bst(node.left, min_val, node.value) and
                self.is_bst(node.right, node.value, max_val))



# Example Usage
tree = BinaryTree()
tree.add_root(4)
tree.add_left(tree.root, 3)
tree.add_right(tree.root, 5)
tree.add_left(tree.root.left, 2)
tree.add_right(tree.root.right, 10)
tree.add_right(tree.root.left, 200)


print("Inorder Traversal:", tree.inorder_traversal(tree.root))
print("Preorder Traversal:", tree.preorder_traversal(tree.root))
print("Postorder Traversal:", tree.postorder_traversal(tree.root))

print(tree.is_bst(tree.root))
