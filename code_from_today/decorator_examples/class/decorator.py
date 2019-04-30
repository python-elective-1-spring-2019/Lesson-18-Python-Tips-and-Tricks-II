
def do_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('This code is executed first')
        func(*args, **kwargs)
        print('This code is executed last')
    return wrapper