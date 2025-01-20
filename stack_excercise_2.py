from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        x = self.container[-1]
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)
    

def is_balanced(val: str):
    stack = Stack()
    symbol_map = {
         "}": "{",
         "]": "[",
         ")": "(",
    }

    for char in val:
        if char in symbol_map.values():
            stack.push(char)
        elif stack.size() != 0 and symbol_map.get(char) == stack.peek():
            stack.pop()
    
    is_balanced = stack.size() == 0
    return is_balanced

print(is_balanced(""))
print(is_balanced("({a+b})"))
print(is_balanced("({a-b(})"))