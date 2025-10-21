import data_py
import logic.student.my_error_give

def list_students():
    for student in data_py.UserData.values():
        if student['role'] != "teacher" and student['role'] != "admin":
            print(f" - {student['name']} ({student['id']}) ")