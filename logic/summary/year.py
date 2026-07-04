import data
import logic
import config
import json


def generate_weekly_summary(id_class):
    t = data.team.read_mainfile(id_class)
    t1 = []
    for i in t["idteam"]:
        t1.append([int(i["id_team"]), []])
        if data.team.check_team(i["id_team"]):
            t3 = data.summary.read(i["id_team"], "semester", 1)
            t4 = data.summary.read(i["id_team"], "semester", 2)
            if t3 and t4:
                t3_students = t3.get("students", [])
                t4_students = t4.get("students", [])
                if len(t3_students) == len(t4_students):
                    for j in range(len(t3_students)):
                        t6 = [t3_students[j][0], t3_students[j][1] + t4_students[j][1], t3_students[j][2]]
                        if t3_students[j][1] > t4_students[j][1]:
                            t1[-1][1].append(t6)
                        elif t3_students[j][1] < t4_students[j][1]:
                            t1[-1][1].append(t6)
                        else:
                            rank_priority = [
                                config.not_achieved, config.achieved, config.medium,
                                config.rather, config.good, config.very_good, config.super_good
                            ]
                            r1 = rank_priority.index(t3_students[j][2]) if t3_students[j][2] in rank_priority else 0
                            r2 = rank_priority.index(t4_students[j][2]) if t4_students[j][2] in rank_priority else 0
                            t1[-1][1].append(t3_students[j] if r1 >= r2 else t4_students[j])

    t5 = {}
    for i in t["idteam"]:
        for j in t1:
            if str(i["id_team"]) == str(j[0]):
                t5[i["id_team"]] = {"students": j[1]}
                break

    data.summary.write(1, t5, "year", id_class)
    return t1
