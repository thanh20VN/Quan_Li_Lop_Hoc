import data_py
import config


def give_error(id):
    teams = data_py.eg.read_egfile("e")
    for er in teams:
        if er["id"] == id:
            return er
    return {"id": 0, "name": "Unknown", "point": 0}


def give_give(id):
    teams = data_py.eg.read_egfile("g")
    for er in teams:
        if er["id"] == id:
            return er
    return {"id": 0, "name": "Unknown", "point": 0}


def _get_class_id(iduser, id_class=None):
    if id_class:
        return id_class
    user = data_py.find_user(iduser)
    if user and isinstance(user, dict):
        return user.get("class_id")
    return None


def _find_user_team(user_id, id_class):
    teams = data_py.team.read_mainfile(id_class)
    for team_info in teams["idteam"]:
        team = data_py.team.read_teamfile(team_info["id_team"])
        if team and user_id in team["members"]:
            return team_info["id_team"], team
    return None, None


def my_errors(iduser, id_class=None):
    id_class = _get_class_id(iduser, id_class)
    if not id_class:
        return []
    teamleider_id, team = _find_user_team(iduser, id_class)
    if not team:
        return []
    idx = team["members"].index(iduser)
    result = []
    for error_id in team["errors"][idx]:
        error_info = give_error(error_id)
        result.append(error_info)
    return result


def my_give(iduser, id_class=None):
    id_class = _get_class_id(iduser, id_class)
    if not id_class:
        return []
    teamleider_id, team = _find_user_team(iduser, id_class)
    if not team:
        return []
    idx = team["members"].index(iduser)
    result = []
    for give_id in team["give"][idx]:
        give_info = give_give(give_id)
        result.append(give_info)
    return result


def cal_errors(iduser, id_class=None):
    m = my_errors(iduser, id_class)
    if not m:
        return 0
    t = 0
    for i in m:
        t += i["point"]
    return t


def cal_give(iduser, id_class=None):
    m = my_give(iduser, id_class)
    # print(m)
    if not m:
        return 0
    t = 0
    for i in m:
        t += i["point"]
    return t


def cal_total(iduser, id_class=None):
    return config.default_point + int(cal_give(iduser, id_class)) - int(cal_errors(iduser, id_class))
