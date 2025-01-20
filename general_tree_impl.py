from enum import Enum

class TraversalType(Enum):
    DFS = 1
    BFS = 2

class Node:
    def __init__(self, val, children = None, parent = None):
        self.value = val
        self.children = []
        self.parent = None

    def add(self, node):
        self.children.append(node)

class GeneralTree:
    def __init__(self, root_value = None):
        self.root = Node(val=root_value)

    def traverse(self):
        node = self.root
        self.print_nodes(node)        
            
    def print_nodes(self, node):
        print(node.value)
        for child in node.children:
            return self.print_nodes(child)

    def find_node(self, root, value):
        if root.value == value:
            return root
        else:
            for child in root.children:
                return self.find_node(child, value)
        
        return None

    def insert(self, val, after):
        node = self.find_node(self.root, after)
        if node:
            node.add(Node(val, parent=node))

    def delete(self, val):
        node = self.find_node(self.root, val)
        

    def search(self, val):
        pass


if __name__ == '__main__':
    tree = GeneralTree(root_value=10)
    tree.traverse()

    tree.insert(20, 10)
    tree.insert(30, 20)
    tree.insert(40, 30)
    tree.insert(50, 40)
    tree.traverse()
