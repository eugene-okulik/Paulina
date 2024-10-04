def repeat_me(count=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(count):
                func(*args, **kwargs)
        return wrapper
    return decorator


@repeat_me(count=8)
def example(text):
    print(text)


example('print me')
