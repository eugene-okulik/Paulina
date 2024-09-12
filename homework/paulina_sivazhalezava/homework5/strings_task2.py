result1 = 'результат операции: 42'
result2 = 'результат операции: 514'
result3 = 'результат работы программы: 9'
number_to_add = 10


number1 = int(result1[result1.index('42'):]) + number_to_add
number2 = int(result2[result2.index('514'):]) + number_to_add
number3 = int(result3[result3.index('9'):]) + number_to_add


print(number1, number2, number3)
