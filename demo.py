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
                t4=data.summary.read(i["id_team"],"week",h+1)
                for j in t4.values(): t5=[j["name"], j["total"], j["ratings"]]
                t3.append(t5)
            t6.append([int(i["id_team"]),t3])
            t3=[]
    for i in range(len(t6)):
        jj=i
        for j in range(1,len(t6[i])):
            # print(t6[i][j])
            t8=[t6[i][j][0][0],0,[[0,"Not achieved"],[0,"Achieved"],[0,"Medium"],[0,"Good"],[0,"Very good"],[0,"Super good"]]]
            for h in t6[i][j]:
                t8[1]+=h[1]
                if h[2]=="Not achieved": t8[2][0][0]+=1
                elif h[2]=="Achieved": t8[2][1][0]+=1
                elif h[2]=="Medium": t8[2][2][0]+=1
                elif h[2]=="Good": t8[2][3][0]+=1
                elif h[2]=="Very good": t8[2][4][0]+=1
                elif h[2]=="Super good": t8[2][5][0]+=1
            for i in range(len(t8[2])):
                for h in range(len(t8[2])):
                    if h>=len(t8[2]): break
                    if t8[2][h][0]==0: t8[2].pop(h)
        t7.append([t6[jj][0],t8])
        # print(t7)
        t7[0][1][2].append([1,'Very good'])
        t7[0][1][2].append([16,'Good'])
        for j in t7:
            for h in range(1,len(j)): j[h][2]=sorted(j[h][2],reverse=True)[0]
        print(t7)

# generate_weekly_summary()