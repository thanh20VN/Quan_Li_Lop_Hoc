import data
import logic.team.add
import logic.team.remove

def create_team(name, teamleider_id):
    teams = {"name": name, "teamleider_id": teamleider_id, "members": [], "errors": [], "give": []}
    data.team.write_teamfile(teamleider_id, teams)
    m=data.team.read_mainfile(teamleider_id)
    m["idteam"].append({"name":name,"id_team":teamleider_id})
    return ValueError("Create team successfully")

def add_member(teamleider_id, user_id):
    if data.team.check_team(teamleider_id):
        teams = data.team.read_teamfile(teamleider_id)
        if user_id not in teams["members"]:
            teams["members"].append(user_id)
            teams["errors"].append([])
            teams["give"].append([])
            data.team.write_teamfile(teamleider_id, teams)
            return ValueError("Successfully add menber")
        else:
            return ValueError("Nember in team")
    else:
        return ValueError("Not find out team")

def remove_member(teamleider_id, user_id):
    if data.team.check_team(teamleider_id):
        teams = data.team.read_teamfile(teamleider_id)
        if user_id in teams["members"]:
            teams["members"].remove(user_id)
            data.team.write_teamfile(teamleider_id, teams)
            return ValueError("Successfully remove menber")
        else:
            return ValueError("Menber in team")
    else:
        return ValueError("Not found out team")

def team(name, teamleider_id):
    if data.team.check_team(teamleider_id):
        return add_member(teamleider_id, teamleider_id)
    else:
        return create_team(name, teamleider_id)