import data
import logic

def create():
    t=data.team.read_mainfile()
    for i in t["idteam"]: 
        data.summary.create(i["id_team"], "year")

def generate_weekly_summary():
    t=data.team.read_mainfile()
    create()
    t1={}
    for i in t["idteam"]: 
        if data.team.check_team(i["id_team"]):
            t2=data.summary.list_summaries(i["id_team"],"semester")
            t3=[]
            for h in range(t2["num"]):
                t4=data.summary.read(i["id_team"],"semester",h+1)
                t5=[]
                for j in t4: t5.append(j["name"],j["ratings"],j["total"])
                t3.append(t5)
            print(t3)