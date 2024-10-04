def operation_decider(func):
    def wrapper(first, second):
        if first < 0 or second < 0:
            return func(first, second, '*')
        elif first == second:
            return func(first, second, '+')
        elif first > second:
            return func(first, second, '-')
        elif second > first:
            return func(first, second, '/')
        else:
            raise ValueError("Unsupported operation")
    return wrapper


@operation_decider
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        if second == 0:
            return "Cannot divide by zero"
        return first / second
    elif operation == '*':
        return first * second
    else:
        return "Unknown operation"


# Запрос входных данных пользователя
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

# Вызываем функцию с введенными числами
result = calc(first_number, second_number)
print(f"Result: {result}")
