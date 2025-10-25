import os
from . import team
from . import eg
from . import summary

if not os.path.exists("./data/User.json"):
    with open("./data/User.json", "w", encoding="utf-8") as f:
        f.write("{}")

UserData = {}

def load_users():
    import json
    with open("./data/User.json", "r", encoding="utf-8") as f:
        global UserData
        UserData = json.load(f)
    return "Tải thông tin thành công."
# y=0
def find_user(id):
    # global y
    # y+=1
    for user in UserData.values():
        # print(user,y)
        if user["id"] == id:
            return {"name": user["name"], "id": user["id"], "role": user["role"]}
    return "Không có tài khoản này."

def find_user_name(name):
    for user in UserData.values():
        if user["name"] == name:
            return {"name": user["name"], "id": user["id"], "role": user["role"]}
    return "Không có tài này."

def create_user(name, password, id, role):
    import json
    UserData[id-1] = {"name": name, "password": password, "id": id, "role": role}
    with open("./data/User.json", "w", encoding="utf-8") as f:
        json.dump(UserData, f, ensure_ascii=False, indent=4)
    return "Tạo tài khoản thành công."

def delete_user(id):
    import json
    if id-1 in UserData:
        del UserData[id-1]
        with open("./data/User.json", "w", encoding="utf-8") as f:
            json.dump(UserData, f, ensure_ascii=False, indent=4)
        return "Xoá tài khoản thành công."
    else:
        return "Không có tài khoản này."


def find_role(role_name):
    list = []
    for user in UserData.values():
        if user["role"] == role_name:
            list.append({"name": user["name"], "id": user["id"], "role": user["role"]})
    return list
