import data_py
import logic.student.my_error_give

def list_students():
    t1=[]
    for student in data_py.UserData.values():
        if student['role'] != "teacher" and student['role'] != "admin":
            t1.append([student['name'],student['id']])
    return t1