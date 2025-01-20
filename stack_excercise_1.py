from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)
    

def reverse_string(val: str):
    stack = Stack()
    for char in val:
        stack.push(char)
    
    reversed = ""
    for char in range(stack.size()):
        reversed += stack.pop()
    
    return reversed


print(reverse_string(""))
print(reverse_string("hello world"))