import data_py
import logic
import config

def generate_weekly_summary():
    t=data_py.team.read_mainfile()
    data_py.summary.create("week")
    t2={}
    for i in t["idteam"]: 
        if data_py.team.check_team(i["id_team"]):
            t1=data_py.team.read_teamfile(i["id_team"])
            t4={}
            for j in t1["members"]:
                t3=data_py.find_user(j)
                tot=logic.student.my_error_give.cal_total(t3["id"])
                if t3["role"]=="student" or t3["role"]=="teamleider" or t3["role"]=="class monitor":
                    if tot<=10: rat=config.not_achieved
                    elif tot>=11 and tot<=20: rat=config.achieved
                    elif tot>=21 and tot<=30: rat=config.medium
                    elif tot>=31 and tot<=50: rat=config.rather
                    elif tot>=51 and tot<=70: rat=config.good
                    elif tot>=71 and tot<=80: rat=config.very_good
                    elif tot>=90: rat=config.super_good
                    t4[t3["id"]] = {
                        "name": t3["name"],
                        "give": logic.student.my_error_give.cal_give(t3["id"]),
                        "error": logic.student.my_error_give.cal_errors(t3["id"]),
                        "total": tot,
                        "ratings": rat
                    }
            data_py.summary.write(i["id_team"], t4, "week")
            t2[t1["teamleider_id"]] = t4
    # data_py.team.remove_give_error()
    t9=data_py.team.read_mainfile()
    for i in t9["idteam"]:
        t8=data_py.team.read_teamfile(i["id_team"])
        le=len(t8["members"])
        t8["errors"]=[]
        t8["give"]=[]
        for j in range(le):
            t8["errors"].append([])
            t8["give"].append([])
        data_py.team.write_teamfile(i["id_team"],t8)
    return t2