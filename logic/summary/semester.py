import data
import logic


def generate_weekly_summary():
    t=data.team.read_mainfile()
    data.summary.create("semester")
    t6=[]
    for i in t["idteam"]: 
        if data.team.check_team(i["id_team"]):
            t2=data.summary.read_main("week")
            t3=[]
            for h in range(t2["num"]):
                t5=[]
                t4=data.summary.read(i["id_team"],"week",h+1)
                for j in t4.values(): t5.append([j["name"], j["total"], j["ratings"]])
                t3.append(t5)
            t6.append([int(i["id_team"]),t3])
            t3=[]
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
                        t7[-1][1].append([student_name, 0, [[0, "Not achieved"], [0, "Achieved"], [0, "Medium"], [0, "Rather"], [0, "Good"], [0, "Very good"], [0, "Super good"]]])
                        l = len(t7[-1][1]) - 1
                    t7[-1][1][l][1] += student_total
                    if rating == "Not achieved": t7[-1][1][l][2][0][0] += 1
                    elif rating == "Achieved": t7[-1][1][l][2][1][0] += 1
                    elif rating == "Medium": t7[-1][1][l][2][2][0] += 1
                    elif rating == "Rather": t7[-1][1][l][2][3][0] += 1
                    elif rating == "Good": t7[-1][1][l][2][4][0] += 1
                    elif rating == "Very good": t7[-1][1][l][2][5][0] += 1
                    elif rating == "Super good": t7[-1][1][l][2][6][0] += 1
    for i in range(len(t7)):
        for j in range(len(t7[i][1])):
            t7[i][1][j][2].sort(reverse=True)
            t7[i][1][j][2] = t7[i][1][j][2][0][1]
    for i in t7: data.summary.write(i[0],{"students":i[1]},"semester")
    # print(t7)
    for i in t["idteam"]: data.summary.remove(i["id_team"], "week")
    with open("./data/summary/{0}/main.json".format("week"), "r", encoding="utf-8") as f:
        import json
        main = json.load(f)
        main["num"] = 0

    with open("./data/summary/{0}/main.json".format("week"), "w", encoding="utf-8") as f:
        json.dump(main, f)
    return t7