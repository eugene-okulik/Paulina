import sys
sys.set_int_max_str_digits(0)


def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def get_fibonacci_number(index):
    fib_gen = fibonacci_generator()
    fib_number = None
    for x in range(index):
        fib_number = next(fib_gen)
    return fib_number


print(get_fibonacci_number(5))
print(get_fibonacci_number(200))
print(get_fibonacci_number(1000))
print(get_fibonacci_number(100000))
