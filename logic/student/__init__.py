import data
import logic.student.my_error_give

def list_students():
    for student in data.UserData.values():
        if student['role'] != "teacher" and student['role'] != "admin":
            print(f" - {student['name']} ({student['id']}) ")