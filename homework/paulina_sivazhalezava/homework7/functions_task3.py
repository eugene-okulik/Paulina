def addition_of_the_number(program_result_string, number_to_add):
    result = int(program_result_string[program_result_string.index(':') + 1:].strip()) + number_to_add
    print(result)


addition_of_the_number('результат: 2', 10)
