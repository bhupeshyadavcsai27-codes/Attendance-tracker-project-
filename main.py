import sqlite3

conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()

# Create Students Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    roll_no TEXT UNIQUE NOT NULL,
    course TEXT NOT NULL
)
""")

# Create Attendance Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS attendance(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    date TEXT,
    status TEXT,
    FOREIGN KEY(student_id) REFERENCES students(id)
)
""")

conn.commit()

# Add Student
name = input("Enter Name: ")
roll_no = input("Enter Roll No: ")
course = input("Enter Course: ")

cursor.execute(
    "INSERT INTO students(name, roll_no, course) VALUES(?,?,?)",
    (name, roll_no, course)
)

conn.commit()

print("Student Added Successfully!")

conn.close()