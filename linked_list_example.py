class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def show_all(self):
        current = self.head
        if current is None:
            print("No elements present")
            return
        
        while current is not None:
            if current.next is None:
                print(current.value)
            else:
                print(current.value, end="->")
            current = current.next

    def insert_at_end(self, value):
        last_node = self.head
        
        if last_node is None:
            self.head = Node(value=value, next=None)
        else:
            while last_node is not None:
                if last_node.next is None:
                    last_node.next = Node(value=value, next=None)
                    return
                
                last_node = last_node.next

    def insert_at_beginning(self, value):
        if self.head is None:
            self.head = Node(value=value, next=None)
        else:
            new_head_node = Node(value=value, next=self.head)
            self.head = new_head_node

    def delete_from_beginning(self):
        next_node = self.head.next
        self.head = next_node

    def delete_from_end(self):
        if self.head.next is None:
            self.head = None
            return
        
        node_before_current = None
        current = self.head

        while current is not None:
            if current.next is None:
                node_before_current.next = None
                return
            
            node_before_current = current
            current = current.next
        

if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.show_all()
    

    linked_list.insert_at_end(10)
    linked_list.insert_at_end(20)
    linked_list.insert_at_end(30)
    linked_list.insert_at_end(40)
    linked_list.insert_at_end(50)
    linked_list.insert_at_end(60)
    linked_list.show_all()

    linked_list.insert_at_beginning(9)
    linked_list.show_all()

    linked_list.delete_from_beginning()
    linked_list.delete_from_beginning()
    linked_list.show_all()

    linked_list.delete_from_end()
    linked_list.delete_from_end()
    linked_list.delete_from_end()
    linked_list.delete_from_end()
    linked_list.show_all()
