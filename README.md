# Attendance Management System

A desktop-based Attendance Management System developed using **Python**, **Tkinter**, and **SQLite**. The application helps educational institutions efficiently manage student records and attendance through an easy-to-use graphical user interface.

## Features

✅ Admin Login System

✅ Add Student Records

✅ View Student Details

✅ Search Student

✅ Mark Attendance

✅ View Attendance Records

✅ Calculate Attendance Percentage

✅ Generate Attendance Reports

✅ Export Attendance Data to CSV

✅ SQLite Database Integration

✅ User-Friendly Tkinter GUI

---

## Technologies Used

* Python
* Tkinter
* SQLite3
* CSV Module

---

## Project Structure

```text
Attendance-Management-System/
│
├── gui.py
├── login.py
├── attendance.db
├── attendance_report.csv
├── README.md
└── faces/
```

---

## Database Schema

### Students Table

| Column  | Type    |
| ------- | ------- |
| id      | INTEGER |
| name    | TEXT    |
| roll_no | TEXT    |
| course  | TEXT    |

### Attendance Table

| Column     | Type    |
| ---------- | ------- |
| id         | INTEGER |
| student_id | INTEGER |
| date       | TEXT    |
| status     | TEXT    |

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/Attendance-Management-System.git
cd Attendance-Management-System
```

### Run the Application

```bash
python login.py
```

or

```bash
python gui.py
```

---

## Login Credentials

Default Admin Credentials:

```text
Username: admin
Password: 1234
```

You can modify these credentials directly in the `login.py` file.

---

## How to Use

1. Login using admin credentials.
2. Add student information.
3. View and search student records.
4. Mark attendance for students.
5. View attendance history.
6. Calculate attendance percentage.
7. Generate reports.
8. Export attendance records to CSV.

---

## Screenshots
### Dashboard
<img width="745" height="723" alt="Screenshot 2026-06-15 214018" src="https://github.com/user-attachments/assets/5e7ca4f2-2494-45cc-b1c9-4f1988f69e6c" />

### Attendance Module

<img width="368" height="346" alt="Screenshot 2026-06-15 214038" src="https://github.com/user-attachments/assets/10d10db0-d724-4092-84ad-355b029d6f5b" />
<img width="863" height="528" alt="Screenshot 2026-06-15 214049" src="https://github.com/user-attachments/assets/77ab1b07-e201-472b-954c-7607b2210131" />
<img width="422" height="402" alt="Screenshot 2026-06-15 214101" src="https://github.com/user-attachments/assets/f4d5f017-8d30-4726-a509-493e15d5c01c" />
<img width="367" height="270" alt="Screenshot 2026-06-15 214111" src="https://github.com/user-attachments/assets/0fd7d25c-a5e3-4c1a-82dc-f8f46059a752" />
<img width="367" height="270" alt="Screenshot 2026-06-15 214111" src="https://github.com/user-attachments/assets/c9eee237-017c-43fd-bae3-9154091dba70" />
<img width="367" height="270" alt="Screenshot 2026-06-15 214111" src="https://github.com/user-attachments/assets/693a2ad0-1cdc-4dfc-8689-134541e95f74" />
<img width="367" height="270" alt="Screenshot 2026-06-15 214111" src="https://github.com/user-attachments/assets/c19a37f6-b15c-4229-88a2-fa3b359aec77" />
<img width="367" height="270" alt="Screenshot 2026-06-15 214111" src="https://github.com/user-attachments/assets/a06bd721-3d72-49c7-8185-8d6f49b238b6" />
<img width="367" height="270" alt="Screenshot 2026-06-15 214111" src="https://github.com/user-attachments/assets/1a712947-c261-4699-b288-e965ff27c5e8" />

---

## Future Enhancements

* Face Recognition Attendance System
* QR Code Based Attendance
* Excel Export (.xlsx)
* Update Student Information
* Delete Student Records
* Attendance Analytics Dashboard
* Email Notifications

---

## Learning Outcomes

This project helped in understanding:

* GUI Development using Tkinter
* Database Management with SQLite
* CRUD Operations
* File Handling in Python
* CSV Data Export
* Modular Programming

---

## Author

**Bhupesh Yadav**

B.Tech CSE Student

---

## License

This project is developed for educational and learning purposes.
