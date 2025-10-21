import os
import json
import shutil

def write(teamleider_id, teams, type):
    with open("./data/summary/{0}/main.json".format(type), "r", encoding="utf-8") as f:
        main = json.load(f)
    if type not in ["week", "semester", "year"]:
        return "Invalid type. Must be 'week', 'semester', or 'year'."
    elif type == "week":
        file_path = "./data/summary/week/Team_{0}/{1}.json".format(teamleider_id, main["num"])
    elif type == "semester":
        file_path = "./data/summary/semester/Team_{0}/{1}.json".format(teamleider_id, main["num"])
    elif type == "year":
        # file_path = "./data/summary/year/Team_{0}/{1}.json".format(teamleider_id
        # , main["num"])
        with open("./data/summary/year.json", "w", encoding="utf-8") as f:
            json.dump(teams, f)
        return
    # Tạo thư mục cha nếu chưa tồn tại
    # os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(teams, f)

def read(teamleider_id, type, id):
    import json
    if type not in ["week", "semester", "year"]:
        return "Invalid type. Must be 'week', 'semester', or 'year'."
    elif type == "week":
        file_path = "./data/summary/week/Team_{0}/{1}.json".format(teamleider_id, id)
    elif type == "semester":
        file_path = "./data/summary/semester/Team_{0}/{1}.json".format(teamleider_id, id)
    elif type == "year":
        # file_path = "./data/summary/year/Team_{0}/{1}.json".format(teamleider_id, id)
        file_path = "./data/summary/year.json"
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"No summary found for teamleider_id {teamleider_id}, type {type}, id {id}")
    else:
        with open(file_path, "r", encoding="utf-8") as f:
            teams = json.load(f)
    if not teams:
        with open(file_path, "r", encoding="utf-8") as f:
            teams = json.load(f)
    return teams

def list_summaries(teamleider_id,type):
    t1={}
    with open("./data/summary/{0}/main.json".format(type), "r", encoding="utf-8") as f:
        import json
        main = json.load(f)
        id = main["num"]
    for i in range(1, id):
        if check(teamleider_id, type, i):
            t1[i]=read(teamleider_id, type, i)
    return t1

def check(teamleider_id, type, id):
    import os
    if type not in ["week", "semester", "year"]:
        return "Invalid type. Must be 'week', 'semester', or 'year'."
    elif type == "week":
        file_path = "./data/summary/week/Team_{0}/{1}.json".format(teamleider_id, id)
    elif type == "semester":
        file_path = "./data/summary/semester/Team_{0}/{1}.json".format(teamleider_id, id)
    elif type == "year":
        file_path = "./data/summary/year/Team_{0}/{1}.json".format(teamleider_id, id)
    return os.path.exists(file_path)

def read_main(type):
    import json
    with open("./data/summary/{0}/main.json".format(type), "r", encoding="utf-8") as f:
        return json.load(f)

def create(type):
    import os
    with open("./data/summary/{0}/main.json".format(type), "r", encoding="utf-8") as f:
        import json
        main = json.load(f)
        id = main["num"] + 1
        main["num"] = id

    with open("./data/summary/{0}/main.json".format(type), "w", encoding="utf-8") as f:
        json.dump(main, f)
    import data_py
    t=data_py.team.read_mainfile()
    for i in t["idteam"]: 
        teamleider_id= i["id_team"]
        if type not in ["week", "semester", "year"]:
            return "Invalid type. Must be 'week', 'semester', or 'year'."
        elif type == "week":
            file_dir = "./data/summary/week/Team_{0}/".format(teamleider_id)
            file_path = "./data/summary/week/Team_{0}/{1}.json".format(teamleider_id, id)
        elif type == "semester":
            file_dir = "./data/summary/semester/Team_{0}/".format(teamleider_id)
            file_path = "./data/summary/semester/Team_{0}/{1}.json".format(teamleider_id, id-1)
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        # with open(file_path, "w", encoding="utf-8") as f: f.write("{}")


def remove(teamleider_id, type):
    import os
    if type not in ["week", "semester"]:
        return "Invalid type. Must be 'week', 'semester', or 'year'."
    else:
        file_path = "./data/summary/{0}/Team_{1}".format(type,teamleider_id)
    if os.path.exists(file_path):
        shutil.rmtree(file_path)