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
    import data
    list = data.find_role("teamleider")
    for teamleider in list:
        if check_team(teamleider["id"]):
            teams = data.team.read_teamfile(teamleider["id"])
            if teams["name"] == teamleider_name:
                return teamleider["id"]

def list_teams(id):
    import data
    if check_team(id):
        teams = read_teamfile(id)
        men = []
        for member_id in teams["members"]:
            member = data.find_user(member_id)
            if member:
                men.append((member['name'], member['id']))
        if not men:
            return "No members found for this teamleider."
        return men
    else:
        return "No team found for this teamleider."