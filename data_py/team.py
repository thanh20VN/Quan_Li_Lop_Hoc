from .supabase_client import supabase
import json


def check_team(teamleider_id):
    response = (
        supabase.table("teams")
        .select("id")
        .eq("teamleider_id", teamleider_id)
        .execute()
    )
    return len(response.data) > 0


def write_teamfile(teamleider_id, teams):
    existing = (
        supabase.table("teams")
        .select("id")
        .eq("teamleider_id", teamleider_id)
        .execute()
    )
    # print(teams)
    team_data = {
        "name": teams.get("name", ""),
        "teamleider_id": teamleider_id,
        "menbers": json.dumps(teams.get("members", [])) if isinstance(teams.get("members", []), list) else teams.get("members", "[]"),
        "errors": json.dumps(teams.get("errors", [])) if isinstance(teams.get("errors", []), list) else teams.get("errors", "[]"),
        "give": json.dumps(teams.get("give", [])) if isinstance(teams.get("give", []), list) else teams.get("give", "[]"),
        "id_class": teams.get("id_class")
    }
    # print(team_data)
    if existing.data:
        supabase.table("teams").update(team_data).eq("teamleider_id", teamleider_id).execute()
    else:
        supabase.table("teams").insert(team_data).execute()


def read_teamfile(teamleider_id):
    response = (
        supabase.table("teams")
        .select("*")
        .eq("teamleider_id", teamleider_id)
        .execute()
    )
    if not response.data:
        return None
    team = response.data[0]
    members = json.loads(team["menbers"]) if team["menbers"] else []
    errors = json.loads(team["errors"]) if team["errors"] else []
    give = json.loads(team["give"]) if team["give"] else []
    return {
        "name": team["name"],
        "teamleider_id": team["teamleider_id"],
        "members": members,
        "errors": errors,
        "give": give,
        "id_class": team.get("id_class")
    }


def read_mainfile(id_class):
    temp = {"idteam": []}
    req = (
        supabase.table("teams")
        .select("name, teamleider_id")
        .eq("id_class", id_class)
        .execute()
    )
    for i in req.data:
        temp["idteam"].append({"name": i["name"], "id_team": i["teamleider_id"]})
    return temp


def find_team(teamleider_name, id_class):
    import data_py
    t = read_mainfile(id_class)
    for team in t["idteam"]:
        h = data_py.team.read_teamfile(team["id_team"])
        if h and h["name"] == teamleider_name:
            return team["id_team"]
    return None


def list_teams(id_class):
    import data_py
    teams = read_mainfile(id_class)
    result = []
    for team_info in teams["idteam"]:
        team = read_teamfile(team_info["id_team"])
        if team and team["members"]:
            for member_id in team["members"]:
                member = data_py.find_user(member_id)
                if member and isinstance(member, dict):
                    result.append((member['name'], member['id']))
    if not result:
        return "Không có thành viên nào."
    return result


def add_member(teamleider_id, user_id):
    team = read_teamfile(teamleider_id)
    if not team:
        return False
    members = team["members"]
    if user_id in members:
        return False
    members.append(user_id)
    team["errors"].append([])
    team["give"].append([])
    write_teamfile(teamleider_id, team)
    return True


def remove_member(teamleider_id, user_id):
    team = read_teamfile(teamleider_id)
    if not team:
        return False
    members = team["members"]
    if user_id not in members:
        return False
    idx = members.index(user_id)
    members.pop(idx)
    team["errors"].pop(idx)
    team["give"].pop(idx)
    write_teamfile(teamleider_id, team)
    return True


def add_user_error(teamleider_id, user_id, error_id):
    team = read_teamfile(teamleider_id)
    if not team:
        return False
    members = team["members"]
    if user_id not in members:
        return False
    idx = members.index(user_id)
    team["errors"][idx].append(error_id)
    write_teamfile(teamleider_id, team)
    return True


def remove_user_error(teamleider_id, user_id, error_id):
    team = read_teamfile(teamleider_id)
    if not team:
        return False
    members = team["members"]
    if user_id not in members:
        return False
    idx = members.index(user_id)
    if error_id in team["errors"][idx]:
        team["errors"][idx].remove(error_id)
        write_teamfile(teamleider_id, team)
        return True
    return False


def add_user_give(teamleider_id, user_id, give_id):
    team = read_teamfile(teamleider_id)
    if not team:
        return False
    members = team["members"]
    if user_id not in members:
        return False
    idx = members.index(user_id)
    team["give"][idx].append(give_id)
    write_teamfile(teamleider_id, team)
    return True


def remove_user_give(teamleider_id, user_id, give_id):
    team = read_teamfile(teamleider_id)
    if not team:
        return False
    members = team["members"]
    if user_id not in members:
        return False
    idx = members.index(user_id)
    if give_id in team["give"][idx]:
        team["give"][idx].remove(give_id)
        write_teamfile(teamleider_id, team)
        return True
    return False


def get_user_errors(teamleider_id, user_id):
    team = read_teamfile(teamleider_id)
    if not team:
        return []
    members = team["members"]
    if user_id not in members:
        return []
    idx = members.index(user_id)
    return team["errors"][idx]


def get_user_gives(teamleider_id, user_id):
    team = read_teamfile(teamleider_id)
    if not team:
        return []
    members = team["members"]
    if user_id not in members:
        return []
    idx = members.index(user_id)
    return team["give"][idx]


def clear_team_errors(teamleider_id):
    team = read_teamfile(teamleider_id)
    if not team:
        return
    team["errors"] = [[] for _ in team["members"]]
    write_teamfile(teamleider_id, team)


def clear_team_gives(teamleider_id):
    team = read_teamfile(teamleider_id)
    if not team:
        return
    team["give"] = [[] for _ in team["members"]]
    write_teamfile(teamleider_id, team)
