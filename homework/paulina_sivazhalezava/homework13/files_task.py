import os
import datetime

current_dir = os.path.dirname(__file__)
print(current_dir)

source_dir = os.path.abspath(os.path.join(current_dir, '..', '..', 'eugene_okulik', 'hw_13'))
source_file = os.path.join(source_dir, 'data.txt')
print(source_dir)

destination_file = os.path.join(current_dir, 'new_data.txt')


with open(source_file, 'r') as file:
    lines = file.readlines()

results = []

for line in lines:
    number_date_part, description_part = line.strip().split(' - ')
    date_str = ' '.join(number_date_part.split(' ')[1:])
    date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')

    if lines.index(line) == 0:
        new_date = date_obj + datetime.timedelta(weeks=1)
        results.append(new_date.strftime('%Y-%m-%d %H:%M:%S.%f'))
    elif lines.index(line) == 1:
        weekday = date_obj.strftime('%A')
        results.append(weekday)
    elif lines.index(line) == 2:
        today = datetime.datetime.now()
        days_ago = (today - date_obj).days
        results.append(f"{days_ago} days ago")

for result in results:
    print(result)

with open(destination_file, 'w') as file:
    for result in results:
        file.write(result + '\n')
