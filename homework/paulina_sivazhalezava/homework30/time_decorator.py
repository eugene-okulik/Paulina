import requests
import time


def decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f'start time: {start_time:.2f}')
        func(*args, **kwargs)
        end_time = time.time()
        print(f'end time: {end_time:.2f}')
        result = end_time - start_time
        print(f'function execution time: {result:.9f}')
    return wrapper


@decorator
def addition(a, b):
    addition_result = a + b
    print(addition_result)

addition(1, 2)


@decorator
def find_occurrence(text, letter):
    if letter in text:
        print(f'letter {letter} is in {text}')
    else:
        print(f'letter {letter} is not in {text}')

find_occurrence('some text', 'e')


@decorator
def get_page():
    page = requests.get('https://envirocenter.org/which-bottles-cans-have-deposits/')
    print(page.status_code)

get_page()
