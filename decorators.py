from functools import wraps

from numpy.ma.core import inner


def log(filename=None):
    """Декоратор, который автоматически отображает начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки"""
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            result = None
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} ok. Result: {result}\n")
                else:
                    print(f"{func.__name__} ok. Result: {result}\n")
            except Exception as e:
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} error: {e}. Inputs:  {args}, {kwargs}\n")
                else:
                    print(f"{func.__name__} error: {e}. Inputs:  {args}, {kwargs}\n")
            return result
        return inner
    return wrapper
