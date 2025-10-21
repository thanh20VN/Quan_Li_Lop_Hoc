import data_py.role as data1
import data_py
import hashlib

def register(name, password, id, role):
    if role not in data1.__init__:
        return "Invalid role"
    if id < 1 or id > 10:
        return "ID must be between 1 and 10"
    for user in data_py.UserData.values():
        if user["id"] == id:
            return "ID already exists"
    password = hashlib.md5(password.encode()).hexdigest()
    return data_py.create_user(name, password, id, role)