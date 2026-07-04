import data_py
import logic.team.add
import logic.team.remove


def create_team(name, teamleider_id, id_class):
    teams = {
        "name": name,
        "teamleider_id": teamleider_id,
        "members": [teamleider_id],
        "errors": [],
        "give": [],
        "id_class": id_class
    }
    data_py.team.write_teamfile(teamleider_id, teams)
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
            id_index = teams["members"].index(user_id)
            teams["errors"].pop(id_index)
            teams["give"].pop(id_index)
            teams["members"].remove(user_id)
            data_py.team.write_teamfile(teamleider_id, teams)
            return "Xoá thành viên thành công"
        else:
            return "Thành viên không có trong nhóm."
    else:
        return "Không tìm thấy nhóm cho người quản lý này."


def team(name, teamleider_id):
    if data_py.team.check_team(teamleider_id):
        return add_member(teamleider_id, teamleider_id)
    else:
        return create_team(name, teamleider_id)
