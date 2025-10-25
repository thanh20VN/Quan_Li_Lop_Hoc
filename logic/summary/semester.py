import data_py
import logic
import config


def generate_weekly_summary():
    t=data_py.team.read_mainfile()
    t6=[]
    for i in t["idteam"]: 
        if data_py.team.check_team(i["id_team"]):
            t2=data_py.summary.read_main("week")
            t3=[]
            t8=data_py.summary.read_main("semester")
            if t8["num"]==0:
                # print(1)
                for h in range(t2["num"]):
                    t5=[]
                    t4=data_py.summary.read(i["id_team"],"week",h+1)
                    for j in t4.values(): t5.append([j["name"], j["total"], j["ratings"]])
                    t3.append(t5)
            elif t8["num"]==1:
                # print(2)
                for h in range(config.semester_1+1,t2["num"]):
                    # print(h)
                    t5=[]
                    t4=data_py.summary.read(i["id_team"],"week",h+1)
                    for j in t4.values(): t5.append([j["name"], j["total"], j["ratings"]])
                    t3.append(t5)
            t6.append([int(i["id_team"]),t3])
            t3=[]
    # print(t6)
    data_py.summary.create("semester")
    t7=[]
    for i in range(len(t6)):
        t7.append([t6[i][0], []])
        for j in range(1, len(t6[i])):
            for h in range(len(t6[i][j])):
                for k in range(len(t6[i][j][h])):
                    student_name = t6[i][j][h][k][0]
                    student_total = t6[i][j][h][k][1]
                    rating = t6[i][j][h][k][2]
                    for l in range(len(t7[-1][1])):
                        if t7[-1][1][l][0] == student_name:
                            break
                    else:
                        t7[-1][1].append([student_name, 0, [[0, config.not_achieved], [0, config.achieved], [0, config.medium], [0, config.rather], [0, config.good], [0, config.very_good], [0, config.super_good]]])
                        l = len(t7[-1][1]) - 1
                    t7[-1][1][l][1] += student_total
                    if rating == config.not_achieved: t7[-1][1][l][2][0][0] += 1
                    elif rating == config.achieved: t7[-1][1][l][2][1][0] += 1
                    elif rating == config.medium: t7[-1][1][l][2][2][0] += 1
                    elif rating == config.rather: t7[-1][1][l][2][3][0] += 1
                    elif rating == config.good: t7[-1][1][l][2][4][0] += 1
                    elif rating == config.very_good: t7[-1][1][l][2][5][0] += 1
                    elif rating == config.super_good: t7[-1][1][l][2][6][0] += 1
    for i in range(len(t7)):
        for j in range(len(t7[i][1])):
            t7[i][1][j][2].sort(reverse=True)
            t7[i][1][j][2] = t7[i][1][j][2][0][1]
    for i in t7: data_py.summary.write(i[0],{"students":i[1]},"semester")
    # print(t7)
    # print(t7)
    # for i in t["idteam"]: data_py.summary.remove(i["id_team"], "week")
    # with open("./data_py/summary/{0}/main.json".format("week"), "r", encoding="utf-8") as f:
    #     import json
    #     main = json.load(f)
    #     main["num"] = 0

    # with open("./data_py/summary/{0}/main.json".format("week"), "w", encoding="utf-8") as f:
    #     json.dump(main, f)
    return t7