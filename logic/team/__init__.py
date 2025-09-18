import data
import logic.team.add

def create_team(name, teamleider_id):
    teams = {"name": name, "teamleider_id": teamleider_id, "members": [], "errors": [], "give": []}
    data.team.write_teamfile(teamleider_id, teams)
    return True

def add_member(teamleider_id, user_id):
    if data.team.check_team(teamleider_id):
        teams = data.team.read_teamfile(teamleider_id)
        if user_id not in teams["members"]:
            teams["members"].append(user_id)
            teams["errors"].append([])
            teams["give"].append([])
            data.team.write_teamfile(teamleider_id, teams)
            return True
        else:
            return False
    else:
        return False

def remove_member(teamleider_id, user_id):
    if data.team.check_team(teamleider_id):
        teams = data.team.read_teamfile(teamleider_id)
        if user_id in teams["members"]:
            teams["members"].remove(user_id)
            data.team.write_teamfile(teamleider_id, teams)
            return True
        else:
            return False
    else:
        return False

def team(name, teamleider_id):
    if data.team.check_team(teamleider_id):
        return add_member(teamleider_id, teamleider_id)
    else:
        return create_team(name, teamleider_id)