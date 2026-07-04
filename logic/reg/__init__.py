import config as data1
import data
import hashlib

def register(name, password, role=None, class_id=None):
    password = hashlib.md5(password.encode()).hexdigest()
    if role is None:
        role = data1.roles[0]
    return data.create_user(name, password, role, class_id)