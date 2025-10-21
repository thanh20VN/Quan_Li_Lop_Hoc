import data_py

def give_error(id):
    teams = data_py.eg.read_egfile("e")
    for er in teams["errors"]:
        if er["id"] == id:
            return er
    return ["None found"]

def give_give(id):
    teams = data_py.eg.read_egfile("g")
    for er in teams["give"]:
        if er["id"] == id:
            return er
    return ["None found"]

def list_errors(id):
    teams = data_py.error.read_errorfile("e")
    for er in teams["errors"]:
        if er["id"] == id:
            print(f" - {er['error']} ")
            return True
    return False

def list_give(id):
    teams = data_py.eg.read_egfile("g")
    for er in teams["give"]:
        if er["id"] == id:
            print(f" - {er['give']} ")
            return True
    return False

def my_errors(iduser):
    import data_py
    t=data_py.team.read_mainfile()
    for team in t["idteam"]:
        h=data_py.team.read_teamfile(team["id_team"])
        if iduser in h["members"]:
            teams = data_py.team.read_teamfile(h["teamleider_id"])
            index = teams["members"].index(iduser)
            if teams["errors"]==[]:
                return ["None found"]
            m = teams["errors"][index]
            a = []
            if len(str(m))==1:
                a.append(give_error(m))
            else:
                print(2)
                for i in m: a.append(give_error(i))
            return a
    return ["None found"]

def my_give(iduser):
    import data_py
    t=data_py.team.read_mainfile()
    for team in t["idteam"]:
        h=data_py.team.read_teamfile(team["id_team"])
        if iduser in h["members"]:
            teams = data_py.team.read_teamfile(h["teamleider_id"])
            index = teams["members"].index(iduser)
            if teams["give"]==[]:
                return ["None found"]
            m = teams["give"][index]
            a = []
            if len(str(m))==1:
                a.append(give_give(m))
            else:
                print(2)
                for i in m: a.append(give_give(i))
            return a
    return ["None found"]

def cal_errors(iduser):
    m = my_errors(iduser)
    if m == ["None found"]:
        return 0
    t=0
    for i in m:
        t+=i["point"]
    return t

def cal_give(iduser):
    m = my_give(iduser)
    if m == ["None found"]:
        return 0
    t=0
    for i in m:
        t+=i["point"]
    return t

def cal_total(iduser):
    return 100+int(cal_give(iduser))-int(cal_errors(iduser))