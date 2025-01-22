def my_decorator(func):
    def wrapper():
        print("Before execution")
        func()
        print("After execution")
    
    return wrapper

@my_decorator
def main_function():
    print("Core function")

main_function()