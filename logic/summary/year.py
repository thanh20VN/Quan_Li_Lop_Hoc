import data_py
import logic


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
                    if t3["students"][j][1] > t4["students"][j][1]: t1[-1][1].append(t3["students"][j])
                    elif t3["students"][j][1] < t4["students"][j][1]: t1[-1][1].append(t4["students"][j])
                    else:
                        rank_priority = ["Not achieved", "Achieved", "Medium", 
                                      "Rather", "Good", "Very good", "Super good"]
                        r1 = rank_priority.index(t3["students"][j][2])
                        r2 = rank_priority.index(t4["students"][j][2])
                        t1[-1][1].append(t3["students"][j] if r1 >= r2 else t4["students"][j])
    # print(t1)
    # for i in t["idteam"]: data_py.summary.remove(i["id_team"], "semester")
    t5={}
    for i in t["idteam"]:
        for j in t1:
            if i["id_team"] == str(j[0]):
                t5[i["id_team"]] = {"students": j[1]}
                break
    # print(t5)
    with open("./data/summary/year.json", "w") as f:
        import json
        json.dump(t5, f, indent=4)

    # with open("./data_py/summary/{0}/main.json".format("semester"), "r", encoding="utf-8") as f:
    #     import json
    #     main = json.load(f)
    #     main["num"] = 0

    # with open("./data_py/summary/{0}/main.json".format("semester"), "w", encoding="utf-8") as f:
    #     json.dump(main, f)
    return t1
    

# generate_weekly_summary()