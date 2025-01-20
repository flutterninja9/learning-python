from collections import deque

class Node:
    def __init__(self, val, parent = None, left = None, right = None):
        self.data = val
        self.parent = parent
        self.left = left
        self.right = right

    def search(self, x):
        if self.data == x:
            return self
        
        if x < self.data and self.left is not None:
            return self.left.search(x)
        
        if x > self.data and self.right is not None:
            return self.right.search(x)

    def get_min(self, node):
        if node is None or node.left is None:
            return node
        else:
            return self.get_min(node.left)

        
    def insert(self, val):
        if self.data == val:
            return self
        if val < self.data:
            if self.left is None:
                self.left = Node(val, parent=self)
            else:
                return self.left.insert(val)
        else:
            if self.right is None:
                self.right = Node(val, parent=self)
            else:
                return self.right.insert(val)
        


class BST:
    def __init__(self, root = None):
        if root is not None:
            self.root = Node(root)
        else:
            self.root = root

    def search(self, key) -> Node:
        if self.root is None:
            return None
        else:
            return self.root.search(key)
        
    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
            return self.root
        else:
            return self.root.insert(val)

    def get_height(self):
        return self.get_height_helper(self.root)

        
    def get_height_helper(self, node):
        if node is None:
            return -1
        else:
            left_height = self.get_height_helper(node.left)
            right_height = self.get_height_helper(node.right)

            return max(left_height, right_height) + 1
    
    def iter_bfs(self):
        if self.root is None:
            print("No elements!")
            return None
        else:
            queue = deque()
            queue.append(self.root)
            while len(queue) != 0:
                first_element = queue.popleft()
                print(first_element.data)
                if first_element.left is not None:
                    queue.append(first_element.left)

                if first_element.right is not None:
                    queue.append(first_element.right)
    
    def inorder(self):
        self.traversal_helper(self.root)
    
    def traversal_helper(self, node):
        if node is None:
            return
        else:
            self.traversal_helper(node.left)
            print(node.data)
            self.traversal_helper(node.right)

    def delete(self, val):
        return self.delete_helper(self.root, val)
    
    def delete_helper(self, node, val):
        if node is None:
            return node
        else:
            if val < node.data:
                node.left = self.delete_helper(node.left, val)
            elif val > node.data:
                node.right = self.delete_helper(node.right, val)
            else:
                # {node} is the actual node to be deleted
                ## Case 1: When node had no child
                if node.right is None and node.left is None:
                    node = None
                ## Case 2: When node had only left child
                elif node.right is None:
                    node = node.left
                ## Case 3: When node had only right child
                elif node.left is None:
                    node = node.right
                ## Case 4: When node had both children
                else:
                    minimum_on_right_side = node.get_min(node.right)
                    node.data = minimum_on_right_side.data
                    node.right = self.delete_helper(minimum_on_right_side, val)

            return node


                
        

if __name__ == '__main__':
    bst = BST()
    bst.insert(20)
    bst.insert(15)
    bst.insert(25)
    bst.insert(15)
    bst.insert(21)
    bst.insert(16)
    bst.insert(22)
    bst.insert(150)

    # print(f'{bst.search(222) is not None}')
    # print(f'{bst.search(20) is not None}')
    # print(bst.get_height())

    bst.inorder()

    bst.delete(15)
    bst.delete(16)
    bst.delete(150)
    bst.delete(21)

    print("----")

    bst.inorder()