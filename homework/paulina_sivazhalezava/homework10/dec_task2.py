def repeat_me(func):
    def wrapper(*args, **kwargs):
        count = kwargs.get('count', 1)
        if 'count' in kwargs:
            del kwargs['count']

        result = None
        for _ in range(count):
            result = func(*args, **kwargs)
        return result

    return wrapper


@repeat_me
def example(text):
    print(text)


example('print me', count=4)
