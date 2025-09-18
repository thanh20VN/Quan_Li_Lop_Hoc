import data

def give_error(id):
    teams = data.eg.read_egfile("e")
    for er in teams["errors"]:
        if er["id"] == id:
            return er
    return ["None found"]

def give_give(id):
    teams = data.eg.read_egfile("g")
    for er in teams["give"]:
        if er["id"] == id:
            return er
    return ["None found"]

def list_errors(id):
    teams = data.error.read_errorfile("e")
    for er in teams["errors"]:
        if er["id"] == id:
            print(f" - {er['error']} ")
            return True
    return False

def list_give(id):
    teams = data.eg.read_egfile("g")
    for er in teams["give"]:
        if er["id"] == id:
            print(f" - {er['give']} ")
            return True
    return False

def my_errors(iduser):
    import data
    t=data.team.read_mainfile()
    for team in t["idteam"]:
        h=data.team.read_teamfile(team["id_team"])
        if iduser in h["members"]:
            teams = data.team.read_teamfile(h["teamleider_id"])
            index = teams["members"].index(iduser)
            m = teams["errors"][index]
            a = []
            for i in m: a.append(give_error(i))
            return a
    return ["None found"]

def my_give(iduser):
    import data
    t=data.team.read_mainfile()
    for team in t["idteam"]:
        h=data.team.read_teamfile(team["id_team"])
        if iduser in h["members"]:
            teams = data.team.read_teamfile(h["teamleider_id"])
            index = teams["members"].index(iduser)
            m = teams["give"][index]
            a = []
            for i in m: a.append(give_give(i))
            return a
    return ["None found"]

def cal_errors(iduser):
    m = my_errors(iduser)
    t=0
    for i in m:
        t+=i["point"]
    return t

def cal_give(iduser):
    m = my_give(iduser)
    t=0
    for i in m:
        t+=i["point"]
    return t

def cal_total(iduser):
    return 100+int(cal_give(iduser))-int(cal_errors(iduser))