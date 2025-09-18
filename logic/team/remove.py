import data

def remove_error(teamleider_id, student_id, error_id):
    if data.team.check_team(teamleider_id):
        teams = data.team.read_teamfile(teamleider_id)
        if student_id in teams["members"]:
            for error in teams["errors"]:
                if error[0] == error_id and error[1] == student_id:
                    teams["errors"].remove(error)
                    data.team.write_teamfile(teamleider_id, teams)
                    return True
            return False
        else:
            raise ValueError("Student is not in your team.")
    else:
        raise FileNotFoundError("No team found for this teamleider.")
    
def remove_give(teamleider_id, student_id, give_id):
    if data.team.check_team(teamleider_id):
        teams = data.team.read_teamfile(teamleider_id)
        if student_id in teams["members"]:
            for give in teams["give"]:
                if give[0] == give_id and give[1] == student_id:
                    teams["give"].remove(give)
                    data.team.write_teamfile(teamleider_id, teams)
                    return True
            return False
        else:
            raise ValueError("Student is not in your team.")
    else:
        raise FileNotFoundError("No team found for this teamleider.")