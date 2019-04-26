


def decorator(func):
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator

"""
    The folder algorithm_time_overview/ contains some algorithms.
    The timer functionality in the word_count.py could be moved to a decorator function and the decorated to the algorithms.
    You job is to make this work.

"""





