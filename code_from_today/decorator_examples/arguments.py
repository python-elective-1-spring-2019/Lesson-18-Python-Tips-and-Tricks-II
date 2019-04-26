def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        func(*args, **kwargs)
        print("Something is happening after the function is called.")
    return wrapper


@my_decorator
def say_whee(sound):
    print(f'The sound of {sound}')


@my_decorator
def func():
    print('Static message')


@my_decorator
def third(s1, s2):
    print(f'{s1}, {s2}')

# say_whee = my_decorator(say_whee)
