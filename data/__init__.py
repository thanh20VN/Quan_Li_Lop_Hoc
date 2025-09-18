import os
import data.team
import data.role
import data.eg
import data.summary

if not os.path.exists("./data/User.json"):
    with open("./data/User.json", "w", encoding="utf-8") as f:
        f.write("{}")

UserData = {}

def load_users():
    import json
    with open("./data/User.json", "r", encoding="utf-8") as f:
        global UserData
        UserData = json.load(f)
        return True

def find_user(id):
    for user in UserData.values():
        if user["id"] == id:
            return {"name": user["name"], "id": user["id"], "role": user["role"]}
    return False

def find_user_name(name):
    for user in UserData.values():
        if user["name"] == name:
            return {"name": user["name"], "id": user["id"], "role": user["role"]}
    return False

def create_user(name, password, id, role):
    import json
    UserData[id-1] = {"name": name, "password": password, "id": id, "role": role}
    with open("./data/User.json", "w", encoding="utf-8") as f:
        json.dump(UserData, f)
    return True

def delete_user(id):
    import json
    if id-1 in UserData:
        del UserData[id-1]
        with open("./data/User.json", "w", encoding="utf-8") as f:
            json.dump(UserData, f)
        return True
    else:
        return False


def find_role(role_name):
    list = []
    for user in UserData.values():
        if user["role"] == role_name:
            list.append({"name": user["name"], "id": user["id"], "role": user["role"]})
    return list