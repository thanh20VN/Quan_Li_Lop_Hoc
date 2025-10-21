import data_py
import logic.team.add
import logic.team.remove

def create_team(name, teamleider_id):
    teams = {"name": name, "teamleider_id": teamleider_id+1, "members": [teamleider_id+1], "errors": [[]], "give": [[]]}
    data_py.team.write_teamfile(teamleider_id+1, teams)
    m=data_py.team.read_mainfile()
    m["idteam"].append({"name":name,"id_team":teamleider_id+1})
    data_py.team.write_mainfile(m)
    return "Tạo team thành công."

def add_member(teamleider_id, user_id):
    if data_py.team.check_team(teamleider_id):
        teams = data_py.team.read_teamfile(teamleider_id)
        if user_id not in teams["members"]:
            teams["members"].append(user_id)
            teams["errors"].append([])
            teams["give"].append([])
            data_py.team.write_teamfile(teamleider_id, teams)
            return "Thêm thành viên thành công"
        else:
            return "Thành viên đã có trong team"
    else:
        return "Không tìm thấy team"

def remove_member(teamleider_id, user_id):
    if data_py.team.check_team(teamleider_id):
        teams = data_py.team.read_teamfile(teamleider_id)
        if user_id in teams["members"]:
            teams["members"].remove(user_id)
            data_py.team.write_teamfile(teamleider_id, teams)
            return "Successfully remove menber"
        else:
            return "Menber in team"
    else:
        return "Not found out team"

def team(name, teamleider_id):
    if data_py.team.check_team(teamleider_id):
        return add_member(teamleider_id, teamleider_id)
    else:
        return create_team(name, teamleider_id)