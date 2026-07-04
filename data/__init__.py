from .supabase_client import supabase

from . import team
from . import eg
from . import summary


def UserData(id_class=None):
    if id_class is None:
        response = (
            supabase.table("users")
            .select("id, name, role")
            .execute()
        )
    else:
        response = (
            supabase.table("users")
            .select("id, name, role")
            .eq("id_class", id_class)
            .execute()
        )
    result = {}
    for user in response.data:
        result[user["id"]] = {"name": user["name"], "id": user["id"], "role": user["role"]}
    return result


def find_user(id):
    # if id==None: return None
    tmp=None
    for user in supabase.table("users").select("name, id, role, class_id").execute().data:
        if user["id"] == id:
            tmp={"name": user["name"], "id": user["id"], "role": user["role"], "class_id": user["class_id"]}
    if tmp!=None:
        return tmp
    else:
        return "Không có tài khoản này."


def find_user_name(name):
    for user in supabase.table("users").select("name, password, id, role").execute().data:
        if user["name"] == name:
            return {"name": user["name"], "id": user["id"], "role": user["role"]}
    return "Không có tài này."


def create_user(name, password, role, class_id=None):
    response = (
        supabase.table("users")
        .insert({"name": name, "password": password, "role": role, "class_id": class_id})
        .execute()
    )
    if response:
        return ("Tạo tài khoản thành công.", response.data[0]["id"])


def delete_user(id):
    response = (
        supabase.table("users")
        .delete()
        .eq("id", id)
        .execute()
    )
    return "Xoá tài khoản thành công."


def find_role(role_name, id_class=None):
    users = UserData(id_class)
    result = []
    for user in users.values():
        if user["role"] == role_name:
            result.append({"name": user["name"], "id": user["id"], "role": user["role"]})
    return result
