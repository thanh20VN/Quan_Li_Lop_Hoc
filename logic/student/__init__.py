import data
import logic.student.my_error_give

def list_students():
    t1=[]
    for student in data.UserData.values():
        if student['role'] != "teacher" and student['role'] != "admin":
            t1.append([student['name'],student['id']])
    return t1