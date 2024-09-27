import random


def quick_money():
    salary = int(input('Please, enter your salary: '))
    bonus_add = random.choice([True, False])
    if bonus_add:
        bonus_quantity = random.randint(100, 500)
        salary += bonus_quantity
        print(f"Your bonus is ${bonus_quantity}, salary with bonus is ${salary}")
    else:
        print(f"You've got no bonus, your salary is {salary}")


quick_money()
