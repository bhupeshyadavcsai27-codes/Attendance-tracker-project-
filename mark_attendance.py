import sqlite3
from datetime import date

conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()

# Show students
cursor.execute("SELECT * FROM students")

students = cursor.fetchall()

print("\nStudent List")
print("-" * 40)

for student in students:
    print(student)

student_id = input("\nEnter Student ID: ")
status = input("Enter Status (Present/Absent): ")

cursor.execute(
    "INSERT INTO attendance(student_id, date, status) VALUES(?,?,?)",
    (student_id, str(date.today()), status)
)

conn.commit()

print("Attendance Marked Successfully!")

conn.close()