import data
import logic


def generate_weekly_summary():
    t=data.team.read_mainfile()
    # data.summary.create("semester")
    t1=[]
    for i in t["idteam"]: 
        if data.team.check_team(i["id_team"]):
            t2=data.summary.read_main("semester")
            t3=data.summary.read(i["id_team"],"semester",1)
            t4=data.summary.read(i["id_team"],"semester",2)
            print(t3)
            print(t4)
            print(i["id_team"])

generate_weekly_summary()