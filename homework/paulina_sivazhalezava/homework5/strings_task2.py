result1 = 'результат операции: 42'
result2 = 'результат операции: 514'
result3 = 'результат работы программы: 9'


number1 = int(result1[result1.index(':') + 1:].strip()) + 10
number2 = int(result2[result2.index(':') + 1:].strip()) + 10
number3 = int(result3[result3.index(':') + 1:].strip()) + 10


print(number1, number2, number3)
