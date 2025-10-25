import config as data1
import data_py
import hashlib

def register(name, password, id, role):
    if role not in data1.roles:
        return "Không có vai trò đó"
    for user in data_py.UserData.values():
        if user["id"] == id:
            return "ID này đã có sẵn"
    password = hashlib.md5(password.encode()).hexdigest()
    return data_py.create_user(name, password, id, role)