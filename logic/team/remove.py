import data_py

def remove_error(teamleider_id, student_id, error_id):
    if data_py.team.check_team(teamleider_id):
        teams = data_py.team.read_teamfile(teamleider_id)
        if student_id in teams["members"]:
            t1=teams["members"].index(student_id)
            t2=teams["errors"][t1]
            for i in range(0,len(t2)):
                if str(i) == str(error_id):
                    teams["errors"][t1].pop(i)
                    data_py.team.write_teamfile(teamleider_id, teams)
                    return True
            return False
        else:
            return "Thành viên không có trong nhóm của bạn."
    else:
        return "Không tìm thấy nhóm cho người quản lý này."
    
def remove_give(teamleider_id, student_id, give_id):
    if data_py.team.check_team(teamleider_id):
        teams = data_py.team.read_teamfile(teamleider_id)
        if student_id in teams["members"]:
            for give in teams["give"]:
                if give[0] == give_id and give[1] == student_id:
                    teams["give"].remove(give)
                    data_py.team.write_teamfile(teamleider_id, teams)
                    return True
            return False
        else:
            return "Thành viên không có trong nhóm của bạn."
    else:
        return "Không tìm thấy nhóm cho người quản lý này."