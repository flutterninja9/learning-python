import time

def sayHello():
    print("Hello")

def returnsHello(): 
    return "Hello"

sayHello()
print(returnsHello())
time.sleep(2)
sayHello()
print(returnsHello())