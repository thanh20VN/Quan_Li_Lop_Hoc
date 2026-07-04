import data


def remove_error(teamleider_id, student_id, error_id):
    if data.team.check_team(teamleider_id):
        teams = data.team.read_teamfile(teamleider_id)
        if student_id in teams["members"]:
            result = data.team.remove_user_error(teamleider_id, student_id, error_id)
            if result:
                return True
            else:
                return "Không tìm thấy lỗi cần xoá."
        else:
            return "Thành viên không có trong nhóm của bạn."
    else:
        return "Không tìm thấy nhóm cho người quản lý này."


def remove_give(teamleider_id, student_id, give_id):
    if data.team.check_team(teamleider_id):
        teams = data.team.read_teamfile(teamleider_id)
        if student_id in teams["members"]:
            result = data.team.remove_user_give(teamleider_id, student_id, give_id)
            if result:
                return True
            else:
                return "Không tìm thấy điểm cộng cần xoá."
        else:
            return "Thành viên không có trong nhóm của bạn."
    else:
        return "Không tìm thấy nhóm cho người quản lý này."
