import data


def add_error(teamleider_id, user_id, error_id):
    if data.team.check_team(teamleider_id):
        teams = data.team.read_teamfile(teamleider_id)
        if user_id in teams["members"]:
            return data.team.add_user_error(teamleider_id, user_id, error_id)
        else:
            return False
    else:
        return False


def add_give(teamleider_id, user_id, give_id):
    if data.team.check_team(teamleider_id):
        teams = data.team.read_teamfile(teamleider_id)
        if user_id in teams["members"]:
            return data.team.add_user_give(teamleider_id, user_id, give_id)
        else:
            return False
    else:
        return False
