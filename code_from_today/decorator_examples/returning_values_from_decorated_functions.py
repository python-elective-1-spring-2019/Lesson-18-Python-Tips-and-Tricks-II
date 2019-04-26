def do_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        #func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper


@do_twice
def say_whee():
    print(f"Whee!")

@do_twice
def greet(name):
    print(f"Hello {name}")

@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}" # explicit return, but none in wrapper