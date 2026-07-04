import config as data1
import data_py
import hashlib

def register(name, password, role=None, class_id=None):
    password = hashlib.md5(password.encode()).hexdigest()
    if role is None:
        role = data1.roles[0]
    return data_py.create_user(name, password, role, class_id)