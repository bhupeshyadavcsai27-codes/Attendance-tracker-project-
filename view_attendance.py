import sqlite3

conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()

cursor.execute("""
SELECT students.name,
       attendance.date,
       attendance.status
FROM attendance
JOIN students
ON students.id = attendance.student_id
""")

records = cursor.fetchall()

print("\nAttendance Records")
print("-" * 50)

for record in records:
    print(record)

conn.close()