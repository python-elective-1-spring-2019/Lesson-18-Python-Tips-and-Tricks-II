import decorator

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('This code is executed first')
        func(*args, **kwargs)
        print('This code is executed last')
    return wrapper

@my_decorator
def say_whee(name):
    print('Hello ', name)

@my_decorator
def greet():
    print('Static method')


"""
    Make new module with decorator function called do_twice
    This functinn should execute the decorated function twice

"""