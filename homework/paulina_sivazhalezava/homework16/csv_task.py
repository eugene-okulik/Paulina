import os
import csv
import mysql.connector as mysql
import dotenv

dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)


current_dir = os.path.dirname(__file__)
source_dir = os.path.abspath(os.path.join(current_dir, '..', '..', 'eugene_okulik', 'Lesson_16', 'hw_data'))
source_file = os.path.join(source_dir, 'data.csv')

with open(source_file, newline='\n') as csv_file:
    file_data = csv.DictReader(csv_file)
    data = []
    for row in file_data:
        name, second_name, group_title, book_title, subject_title, lesson_title, mark_value = row
        data.append(row)

cursor = db.cursor()

data_missing = []
for row in data:
    cursor.execute("""
        SELECT * FROM students
        LEFT JOIN books ON students.id = books.taken_by_student_id
        LEFT JOIN `groups` ON students.group_id = `groups`.id
        LEFT JOIN marks ON students.id = marks.student_id
        LEFT JOIN lessons ON marks.lesson_id = lessons.id
        LEFT JOIN subjets ON lessons.subject_id = subjets.id
        WHERE students.name = %s AND students.second_name = %s AND groups.title = %s AND books.title = %s
        AND subjets.title = %s AND lessons.title = %s AND marks.value = %s
        """, (row['name'], row['second_name'], row['group_title'],
              row['book_title'], row['subject_title'], row['lesson_title'], row['mark_value']))
    full_data = cursor.fetchall()
    if cursor.rowcount == 0:
        data_missing.append(row)
print("Data missing: ", data_missing)
db.commit()

cursor.close()
db.close()
