from openpyxl import Workbook
import csv
import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
from datetime import date

# ---------------- DATABASE ----------------
conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    roll_no TEXT UNIQUE NOT NULL,
    course TEXT NOT NULL
)
""")

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

# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("Attendance Management System")
root.geometry("600x550")


# ---------------- ADD STUDENT ----------------
def add_student():
    win = tk.Toplevel(root)
    win.title("Add Student")
    win.geometry("300x250")

    tk.Label(win, text="Name").pack()
    name_entry = tk.Entry(win)
    name_entry.pack()

    tk.Label(win, text="Roll No").pack()
    roll_entry = tk.Entry(win)
    roll_entry.pack()

    tk.Label(win, text="Course").pack()
    course_entry = tk.Entry(win)
    course_entry.pack()

    def save():
        try:
            cursor.execute(
                "INSERT INTO students(name, roll_no, course) VALUES(?,?,?)",
                (name_entry.get(), roll_entry.get(), course_entry.get())
            )
            conn.commit()
            messagebox.showinfo("Success", "Student Added")
            win.destroy()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Roll No already exists")

    tk.Button(win, text="Save", command=save).pack(pady=10)


# ---------------- VIEW STUDENTS ----------------
def view_students():
    win = tk.Toplevel(root)
    win.title("Students")
    win.geometry("700x400")

    tree = ttk.Treeview(win, columns=("ID", "Name", "Roll", "Course"), show="headings")

    for col in ("ID", "Name", "Roll", "Course"):
        tree.heading(col, text=col)

    tree.pack(fill="both", expand=True)

    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        tree.insert("", tk.END, values=row)


# ---------------- UPDATE STUDENT ----------------
def update_student():
    win = tk.Toplevel(root)
    win.title("Update Student")
    win.geometry("350x300")

    tk.Label(win, text="Roll No").pack()
    roll_entry = tk.Entry(win)
    roll_entry.pack()

    tk.Label(win, text="New Name").pack()
    name_entry = tk.Entry(win)
    name_entry.pack()

    tk.Label(win, text="New Course").pack()
    course_entry = tk.Entry(win)
    course_entry.pack()

    def update():
        cursor.execute("""
            UPDATE students
            SET name=?, course=?
            WHERE roll_no=?
        """, (name_entry.get(), course_entry.get(), roll_entry.get()))

        conn.commit()
        messagebox.showinfo("Success", "Student Updated")

    tk.Button(win, text="Update", command=update).pack(pady=10)


# ---------------- DELETE STUDENT ----------------
def delete_student():
    win = tk.Toplevel(root)
    win.title("Delete Student")
    win.geometry("300x200")

    tk.Label(win, text="Enter Roll No").pack()
    roll_entry = tk.Entry(win)
    roll_entry.pack()

    def delete():
        cursor.execute("DELETE FROM students WHERE roll_no=?", (roll_entry.get(),))
        conn.commit()
        messagebox.showinfo("Deleted", "Student Deleted")

    tk.Button(win, text="Delete", command=delete).pack(pady=10)


# ---------------- MARK ATTENDANCE ----------------
def mark_attendance():
    win = tk.Toplevel(root)
    win.title("Mark Attendance")
    win.geometry("300x220")

    tk.Label(win, text="Student ID").pack()
    id_entry = tk.Entry(win)
    id_entry.pack()

    tk.Label(win, text="Status").pack()
    status_entry = tk.Entry(win)
    status_entry.pack()

    def save():
        cursor.execute("""
            INSERT INTO attendance(student_id, date, status)
            VALUES(?,?,?)
        """, (id_entry.get(), str(date.today()), status_entry.get()))

        conn.commit()
        messagebox.showinfo("Success", "Attendance Marked")

    tk.Button(win, text="Save", command=save).pack(pady=10)


# ---------------- VIEW ATTENDANCE ----------------
def view_attendance():
    win = tk.Toplevel(root)
    win.title("Attendance")
    win.geometry("800x400")

    tree = ttk.Treeview(win, columns=("Name", "Date", "Status"), show="headings")

    for col in ("Name", "Date", "Status"):
        tree.heading(col, text=col)

    tree.pack(fill="both", expand=True)

    cursor.execute("""
        SELECT students.name, attendance.date, attendance.status
        FROM attendance
        JOIN students ON students.id = attendance.student_id
    """)

    for row in cursor.fetchall():
        tree.insert("", tk.END, values=row)


# ---------------- DELETE ATTENDANCE ----------------
def delete_attendance():
    win = tk.Toplevel(root)
    win.title("Delete Attendance")
    win.geometry("300x200")

    tk.Label(win, text="Attendance ID").pack()
    id_entry = tk.Entry(win)
    id_entry.pack()

    def delete():
        cursor.execute("DELETE FROM attendance WHERE id=?", (id_entry.get(),))
        conn.commit()
        messagebox.showinfo("Deleted", "Attendance Record Deleted")

    tk.Button(win, text="Delete", command=delete).pack()


# ---------------- EXPORT CSV ----------------
def export_csv():
    cursor.execute("""
        SELECT students.name, students.roll_no, students.course,
               attendance.date, attendance.status
        FROM attendance
        JOIN students ON students.id = attendance.student_id
    """)

    data = cursor.fetchall()

    with open("attendance_report.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Roll", "Course", "Date", "Status"])
        writer.writerows(data)

    messagebox.showinfo("Success", "CSV Exported")


# ---------------- EXPORT EXCEL ----------------
def export_excel():
    cursor.execute("""
        SELECT students.name, students.roll_no, students.course,
               attendance.date, attendance.status
        FROM attendance
        JOIN students ON students.id = attendance.student_id
    """)

    data = cursor.fetchall()

    wb = Workbook()
    ws = wb.active

    ws.append(["Name", "Roll No", "Course", "Date", "Status"])

    for row in data:
        ws.append(row)

    wb.save("attendance_report.xlsx")

    messagebox.showinfo("Success", "Excel Exported Successfully")

# ---------------- UI ----------------
title = tk.Label(root, text="Attendance Management System", font=("Arial", 16, "bold"))
title.pack(pady=20)

tk.Button(root, text="Add Student", width=25, command=add_student).pack(pady=3)
tk.Button(root, text="View Students", width=25, command=view_students).pack(pady=3)
tk.Button(root, text="Update Student", width=25, command=update_student).pack(pady=3)
tk.Button(root, text="Delete Student", width=25, command=delete_student).pack(pady=3)

tk.Button(root, text="Mark Attendance", width=25, command=mark_attendance).pack(pady=3)
tk.Button(root, text="View Attendance", width=25, command=view_attendance).pack(pady=3)
tk.Button(root, text="Delete Attendance", width=25, command=delete_attendance).pack(pady=3)

tk.Button(root, text="Export CSV", width=25, command=export_csv).pack(pady=3)
tk.Button(root, text="Export Excel", width=25, command=export_excel).pack(pady=3)

tk.Button(root, text="Exit", width=25, command=root.destroy).pack(pady=5)

root.mainloop()
conn.close()