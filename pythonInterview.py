#decorator example
def logger(func):
    def wrapper():
        print("Function is being called")
        return func()
    return wrapper
@logger
def say_hello():
    print("Hello, World!")

say_hello()
