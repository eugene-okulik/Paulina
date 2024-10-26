import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor()


cursor.execute("INSERT INTO students (name, second_name) values ('Kot', 'Chorny')")
student_id = cursor.lastrowid
print(f"Inserted student ID: {student_id}")

cursor.execute("INSERT INTO `groups` (title, start_date, end_date) VALUES ('Koty', '2023-08-01', '2040-09-30')")
group_id = cursor.lastrowid
print(f"Inserted group ID: {group_id}")

cursor.execute("UPDATE students SET group_id = %s WHERE id = %s", (group_id, student_id))

books = ['Ohota i rybalka', 'Podvyznye igry', 'Kak ponyat cheloveka']
for title in books:
    cursor.execute("INSERT INTO books (title, taken_by_student_id) values (%s, %s)", (title, student_id))

cursor.execute("INSERT INTO subjets (title) values ('Ohota na rybov')")
subject_id1 = cursor.lastrowid
cursor.execute("INSERT INTO subjets (title) values ('Ohota na myshei')")
subject_id2 = cursor.lastrowid
print(f"Inserted subject IDs: {subject_id1}, {subject_id2}")

lessons = [
    ('Vidy myshei', subject_id2),
    ('Kak poymat mysh', subject_id2),
    ('Vidy rybov', subject_id1),
    ('Poymat soma', subject_id1)
]
for title, subject_id in lessons:
    cursor.execute("INSERT INTO lessons (title, subject_id) values (%s, %s)", (title, subject_id))
    lesson_id = cursor.lastrowid
    cursor.execute("INSERT INTO marks (value, lesson_id, student_id) values ('Kharacho', %s, %s)",
                   (lesson_id, student_id))

cursor.execute("SELECT * FROM marks WHERE student_id = %s", (student_id,))
marks = cursor.fetchall()
print("Marks:", marks)

cursor.execute("SELECT * FROM books WHERE taken_by_student_id = %s", (student_id,))
books = cursor.fetchall()
print("Books:", books)

cursor.execute("""
    SELECT * FROM students
    LEFT JOIN books ON students.id = books.taken_by_student_id
    LEFT JOIN `groups` ON students.group_id = `groups`.id
    LEFT JOIN marks ON students.id = marks.student_id
    LEFT JOIN lessons ON marks.lesson_id = lessons.id
    LEFT JOIN subjets ON lessons.subject_id = subjets.id
    WHERE students.id = %s
    """, (student_id,))
full_data = cursor.fetchall()
print("Full data:", full_data)

db.commit()


cursor.close()
db.close()
