secret_number = 7
while True:
    user_guess = int(input("Угадайте цифру: "))
    if user_guess == secret_number:
        print("Поздравляю! Вы угадали!")
        break
    print("Попробуйте снова.")
