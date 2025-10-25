import data_py
import logic
import config

def generate_weekly_summary():
    t = data_py.team.read_mainfile()
    t1 = []
    for i in t["idteam"]:
        t1.append([int(i["id_team"]), []])
        if data_py.team.check_team(i["id_team"]):
            t3 = data_py.summary.read(i["id_team"], "semester", 1)
            t4 = data_py.summary.read(i["id_team"], "semester", 2)
            if len(t3["students"]) == len(t4["students"]):
                for j in range(len(t3["students"])):
                    # print(t3["students"][j], t4["students"][j])
                    t6=[t3["students"][j][0],t3["students"][j][1]+t4["students"][j][1],t3["students"][j][2]]
                    if t3["students"][j][1] > t4["students"][j][1]: t1[-1][1].append(t6)
                    elif t3["students"][j][1] < t4["students"][j][1]: t1[-1][1].append(t6)
                    else:
                        rank_priority = [config.not_achieved, config.achieved, config.medium, config.rather, config.good, config.very_good, config.super_good]
                        r1 = rank_priority.index(t3["students"][j][2])
                        r2 = rank_priority.index(t4["students"][j][2])
                        t1[-1][1].append(t3["students"][j] if r1 >= r2 else t4["students"][j])
    # print(t1)
    # for i in t["idteam"]: data_py.summary.remove(i["id_team"], "semester")
    t5={}
    # print(t1)
    for i in t["idteam"]:
        # print(i)
        for j in t1:
            # print(j)
            if str(i["id_team"]) == str(j[0]):
                t5[i["id_team"]] = {"students": j[1]}
                break
    # print(t5)
    with open("./data/summary/year.json", "w", encoding="utf-8") as f:
        import json
        # print("write",t5)
        json.dump(t5, f, ensure_ascii=False, indent=4)

    # with open("./data_py/summary/{0}/main.json".format("semester"), "r", encoding="utf-8") as f:
    #     import json
    #     main = json.load(f)
    #     main["num"] = 0

    # with open("./data_py/summary/{0}/main.json".format("semester"), "w", encoding="utf-8") as f:
    #     json.dump(main, f)
    return t1
    

# generate_weekly_summary()