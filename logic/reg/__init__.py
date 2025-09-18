import data.role as data1
import data
import hashlib

def register(name, password, id, role):
    if role not in data1.__init__:
        return "Invalid role"
    if id < 1 or id > 10:
        return "ID must be between 1 and 10"
    for user in data.UserData.values():
        if user["id"] == id:
            return "ID already exists"
    password = hashlib.md5(password.encode()).hexdigest()
    return data.create_user(name, password, id, role)