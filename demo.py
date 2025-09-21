import data
import logic


def generate_weekly_summary():
    t=data.team.read_mainfile()
    t1={}
    t6=[]
    t7=[]
    for i in t["idteam"]: 
        if data.team.check_team(i["id_team"]):
            t2=data.summary.read_main("week")
            t3=[]
            for h in range(t2["num"]):
                t5=[]
                t4=data.summary.read(i["id_team"],"week",h+1)
                for j in t4.values():
                    # print(j)
                    t5.append([j["name"], j["total"], j["ratings"]])
                # print(t5)
                t3.append(t5)
            t6.append([int(i["id_team"]),t3])
            t3=[]
    # print(t6[0])
    for i in range(len(t6)):
        for j in range(1,len(t6[i])):
            print(t6[i][j])

generate_weekly_summary()