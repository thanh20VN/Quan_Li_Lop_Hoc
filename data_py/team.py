def check_team(teamleider_id):
    import os
    return os.path.exists("./data/team/Team_{0}.json".format(teamleider_id))

def write_teamfile(teamleider_id, teams):
    import json
    with open("./data/team/Team_{0}.json".format(teamleider_id), "w", encoding="utf-8") as f:
        json.dump(teams, f)

def write_mainfile(teams):
    import json
    with open("./data/team/main.json", "w", encoding="utf-8") as f:
        return json.dump(teams, f)

def read_teamfile(teamleider_id):
    import json
    with open("./data/team/Team_{0}.json".format(teamleider_id), "r", encoding="utf-8") as f:
        teams = json.load(f)
    return teams

def read_mainfile():
    import json
    with open("./data/team/main.json", "r", encoding="utf-8") as f:
        teams = json.load(f)
    return teams

def find_team(teamleider_name):
    import data_py
    t=read_mainfile()
    for team in t["idteam"]:
        h=data_py.team.read_teamfile(team["id_team"])
        if h["name"]==teamleider_name:
            return team["id_team"]

def list_teams(id):
    import data_py
    if check_team(id):
        teams = read_teamfile(id)
        men = []
        for member_id in teams["members"]:
            member = data_py.find_user(member_id)
            if member:
                men.append((member['name'], member['id']))
        if not men:
            return "Không có thành viên nào."
        return men
    else:
        return "Không tìm thấy team."