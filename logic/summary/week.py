import data
import logic
import config


def generate_weekly_summary(id_class):
    t = data.team.read_mainfile(id_class)
    week_num = data.summary.create("week", id_class)
    t2 = {}
    for i in t["idteam"]:
        if data.team.check_team(i["id_team"]):
            t1 = data.team.read_teamfile(i["id_team"])
            t4 = {"week": week_num}
            for j in t1["members"]:
                t3 = data.find_user(j)
                if isinstance(t3, dict):
                    tot = logic.student.my_error_give.cal_total(t3["id"], id_class)
                    if t3["role"] in [config.roles[3], config.roles[2], config.roles[1]]:
                        if tot <= 10:
                            rat = config.not_achieved
                        elif 11 <= tot <= 20:
                            rat = config.achieved
                        elif 21 <= tot <= 30:
                            rat = config.medium
                        elif 31 <= tot <= 50:
                            rat = config.rather
                        elif 51 <= tot <= 70:
                            rat = config.good
                        elif 71 <= tot <= 80:
                            rat = config.very_good
                        elif tot >= 90:
                            rat = config.super_good
                        else:
                            rat = config.medium
                        t4[t3["id"]] = {
                            "name": t3["name"],
                            "give": logic.student.my_error_give.cal_give(t3["id"], id_class),
                            "error": logic.student.my_error_give.cal_errors(t3["id"], id_class),
                            "total": tot,
                            "ratings": rat
                        }
            data.summary.write(i["id_team"], t4, "week", id_class)
            t2[i["id_team"]] = t4
            data.team.clear_team_errors(i["id_team"])
            data.team.clear_team_gives(i["id_team"])
    return t2
