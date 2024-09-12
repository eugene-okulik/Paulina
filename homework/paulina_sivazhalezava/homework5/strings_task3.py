students = ['Ivanov', 'Petrov', 'Sidorov']

subjects = ['math', 'biology', 'geography']

my_text = 'Students {} study these subjects: {}'


print('Students', ', '.join(students) + ' study these subjects: ' + ', '.join(subjects))
print(my_text.format(' ,'.join(students), ' ,'.join(subjects)))
