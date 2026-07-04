import data_py
import hashlib

def login(username, password):
    users = data_py.supabase.table("users").select("name, password, id, role").execute().data
    password = hashlib.md5(password.encode()).hexdigest()
    for user in users:
        if user['name'] == username and user['password'] == password:
            return "Login successful."
    return "Login failed: Invalid username or password."