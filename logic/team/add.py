import data_py

def add_error(teamleider_id, user_id, error_id):
    if data_py.team.check_team(teamleider_id):
        teams = data_py.team.read_teamfile(teamleider_id)
        if user_id in teams["members"]:
            index = teams["members"].index(user_id)
            teams["errors"][index].append(error_id)
            data_py.team.write_teamfile(teamleider_id, teams)
            return True
        else:
            return False
    else:
        return False
    
def add_give(teamleider_id, user_id, give_id):
    if data_py.team.check_team(teamleider_id):
        teams = data_py.team.read_teamfile(teamleider_id)
        if user_id in teams["members"]:
            index = teams["members"].index(user_id)
            teams["give"][index].append(give_id)
            data_py.team.write_teamfile(teamleider_id, teams)
            return True
        else:
            return False
    else:
        return False