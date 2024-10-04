def say_finish(func):
    def wrapper(*args):
        result = func(*args)
        print('finished')
        return result
    return wrapper


@say_finish
def example(text):
    print(text)

    
example('print me')
