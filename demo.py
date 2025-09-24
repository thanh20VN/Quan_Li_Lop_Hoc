import data
import logic


def generate_weekly_summary():
    t=data.team.read_mainfile()
    t1={}
    t6=[]
    for i in t["idteam"]: 
        if data.team.check_team(i["id_team"]):
            t2=data.summary.read_main("week")
            t3=[]
            for h in range(t2["num"]):
                t5=[]
                t4=data.summary.read(i["id_team"],"week",h+1)
                for j in t4.values():
                    t5.append([j["name"], j["total"], j["ratings"]])
                t3.append(t5)
            t6.append([int(i["id_team"]),t3])
            t3=[]
    t7=[]
    for i in range(len(t6)):
        for j in range(1,len(t6[i])):
            for h in range(len(t6[i][j])):
                for k in range(len(t6[i][j][h])):
                    for l in range(len(t7)):
                        if t7[l][0]==t6[i][j][h][k][0]:break
                        # print(t6[i][j])
                    else:t7.append([t6[i][j][h][k][0],0,[[0,"Not achieved"],[0,"Achieved"],[0,"Medium"],[0,"Rather"],[0,"Good"],[0,"Very good"],[0,"Super good"]]])
                    for l in range(len(t7)):
                        if t7[l][0]==t6[i][j][h][k][0]:
                            t7[l][1]+=t6[i][j][h][k][1]
                            if t6[i][j][h][k][2]=="Not achieved": t7[l][2][0][0]+=1
                            elif t6[i][j][h][k][2]=="Achieved": t7[l][2][1][0]+=1
                            elif t6[i][j][h][k][2]=="Medium": t7[l][2][2][0]+=1
                            elif t6[i][j][h][k][2]=="Rather": t7[l][2][3][0]+=1
                            elif t6[i][j][h][k][2]=="Good": t7[l][2][4][0]+=1
                            elif t6[i][j][h][k][2]=="Very good": t7[l][2][5][0]+=1
                            elif t6[i][j][h][k][2]=="Super good": t7[l][2][6][0]+=1
    for kk in range(len(t7)+10):
        for l in range(len(t7)):
            for g in range(len(t7[l][2])):
                if g==len(t7[l][2]):break
                elif t7[l][2][g][0]==0:
                    t7[l][2].pop(g)
                    break
    # print(t7)
    for i in range(len(t7)):
        t7[i][2].sort(reverse=True)
        t7[i][2]=t7[i][2][0][1]
    print(t7)
    

generate_weekly_summary()