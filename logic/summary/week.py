import data
import logic

def generate_weekly_summary():
    t=data.team.read_mainfile()
    data.summary.create("week")
    t2={}
    for i in t["idteam"]: 
        if data.team.check_team(i["id_team"]):
            t1=data.team.read_teamfile(i["id_team"])
            t4={}
            for j in t1["members"]:
                t3=data.find_user(j)
                tot=logic.student.my_error_give.cal_total(t3["id"])
                if t3["role"]=="student" or t3["role"]=="teamleider" or t3["role"]=="class monitor":
                    if tot<=10: rat="Not achieved"
                    elif tot>=11 and tot<=20: rat="Achieved"
                    elif tot>=21 and tot<=30: rat="Medium"
                    elif tot>=31 and tot<=50: rat="Rather"
                    elif tot>=51 and tot<=70: rat="Good"
                    elif tot>=71 and tot<=80: rat="Very good"
                    elif tot>=90: rat="Super good"
                    t4[t3["id"]] = {
                        "name": t3["name"],
                        "total": tot,
                        "ratings": rat
                    }
            data.summary.write(i["id_team"], t4, "week")
            t2[t1["teamleider_id"]] = t4
    # data.team.remove_give_error()
    t9=data.team.read_mainfile()
    for i in t9["idteam"]:
        t8=data.team.read_teamfile(i["id_team"])
        t8["errors"]=[]
        t8["give"]=[]
        data.team.write_teamfile(i["id_team"],t8)
    return t2