import data
import logic

def create():
    t=data.team.read_mainfile()
    for i in t["idteam"]: 
        data.summary.create(i["id_team"], "year")

def generate_weekly_summary():
    t=data.team.read_mainfile()
    t1={}
    t6=[]
    for i in t["idteam"]: 
        if data.team.check_team(i["id_team"]):
            t2=data.summary.read_main("week")
            t3=[]
            for h in range(t2["num"]):
                t4=data.summary.read(i["id_team"],"week",h+1)
                t3.append(int(i["id_team"]))
                for j in t4.values():
                    t5=[
                        j["name"],
                        j["total"],
                        j["ratings"]
                    ]
                t3.append(t5)
            t6.append(t3)
            t3=[]
    print(t6)

generate_weekly_summary()