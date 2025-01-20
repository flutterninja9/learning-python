from collections import deque
import threading
import time

class Queue:
    
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):
        self.buffer.appendleft(val)
        
    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)
    

def place_order(orders):
    for order in orders:
        queue.enqueue(order)
        time.sleep(0.5)

def serve_order():
    while not queue.is_empty():
        current_order = queue.dequeue()
        print("Got order for:", current_order)
        time.sleep(2)

queue = Queue()
thread_1 = threading.Thread(target= place_order(orders=['pizza', 'samosa', 'pasta', 'biryani', 'burger']))
thread_2 = threading.Thread(target= serve_order)

thread_1.start()
time.sleep(1)
thread_2.start()

thread_1.join()
thread_2.join()