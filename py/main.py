#V0.9 (ADAPTAR EL CODIGO PARA QUE LE DE IGUAL LAS TABULACIONES , COMAS , PUNTOS Y COMAS + OPTIMIZACION)
from tkinter import *
from tkinter import filedialog
from tkinter import scrolledtext
import os
import random
#datos = filedialog.askopenfilename()
try:
    with open("data.txt" , encoding='utf-8') as file:
        lines = file.readlines()
except FileNotFoundError:
    print("The file doesnt exist")
except:
    print("Error trying to open de file")

def last_position(elemento):
    return elemento[-1]

def READTEAMS():
    try:
        global numE
        numE = 0
        teamsL = []
        linesE = lines[lines.index('@@@@@\n') + 1:lines.index('@@@@@-\n')]
        for i in linesE:
            i = i.replace("," , " ").replace("    ", " ").replace(";" , " ")
            i = i.split()
            teamsL.append(i)
            numE += 1
        for i in teamsL:
            JJ = float(i[-3])
            JG = float(i[-2])
            AVE = round(JG / JJ , 3)
            i.append(float(AVE))
        teamsL = sorted(teamsL, key=last_position , reverse=True)

        JGP = float(teamsL[0][-3])
        JPP = float(teamsL[0][-2])
        for i in range(0 , len(teamsL)):
            JGS = float(teamsL[i][-3])
            JPS = float(teamsL[i][-2])
            DIF = round(((JGP - JGS) + (JPS - JPP)) / 2 , 1)
            teamsL[i].append(DIF)
        return teamsL
    except IndexError:
        print("REVISA QUE EL ARCHIVO ESTE EN EL FORMATO CORRECTO")

def READPITCHERS():
    try:
        pitchersCL = []
        lineasP = lines[lines.index('*****\n')+1:lines.index('****-\n')]
        for i in lineasP:
            i = i.replace("," , " ").replace("    ", " ").replace(";" , " ")
            i = i.split()
            pitchersCL.append(i)
        for i in pitchersCL:
            P = float(i[-5])
            BB = float(i[-4])
            H = float(i[-3])
            IL = float(i[-2])
            CL = float(i[-1])
            EFE = round((CL*9) / IL , 2)
            i.append(EFE)
            WHIP = round((BB + H) / IL , 2)
            i.append(WHIP)
            PBB = round(P / BB , 2)
            i.append(PBB)
        return pitchersCL
    except IndexError:
        print("REVISA QUE EL ARCHIVO ESTE EN EL FOMATO CORRECTO")

def LIDSSPI(l):
    fileE = open('leaders/Pitching_Leaders.txt' , 'w')
    fileE.write("Pitching Leaders: \n\n")
    fileE.write("TOP 3 PITCHERS BY EFFECTIVENESS\n")
    topEFE = sorted(l , key=lambda x: float(x[-3]))
    for E in topEFE[:3]:
        add = ""
        playerstat = ""
        IDE = E[0]
        for e in range(0, len(teams)):
            if IDE == teams[e][0]:
                for j in range(1 , len(teams[e]) - 5):
                    add += f"{str(teams[e][j])} "
                playerstat += f"{str(E[2])} " + f"{str(E[3])}" + f" : {str(E[-3])}" 
                fileE.write(f"{add} => {playerstat}\n")
    fileE.write("\n")
    fileE.write("TOP 3 PITCHER BY WHIP\n")
    topWHIP = sorted(l , key=lambda x: float(x[-2]))
    for W in topWHIP[:3]:
        add = ""
        playerstat = ""
        IDW = W[0]
        for w in range(0, len(teams)):
            if IDW == teams[w][0]:
                for j in range(1 , len(teams[w]) - 5):
                    add += f"{str(teams[w][j])} "
                playerstat += f"{str(W[2])} " + f"{str(W[3])}" + f" : {str(W[-2])}" 
                fileE.write(f"{add} => {playerstat}\n")
    fileE.write("\n")
    fileE.write("TOP 3 PITCHERS BY P/BB\n")
    topPBB = sorted(l , key=lambda x: float(x[-1]) , reverse=True)
    for P in topPBB[:3]:
        add = ""
        playerstat = ""
        IDP = P[0]
        for p in range(0, len(teams)):
            if IDP == teams[p][0]:
                for j in range(1 , len(teams[p]) - 5):
                    add += f"{str(teams[p][j])} "
                playerstat += f"{str(P[2])} " + f"{str(P[3])}" + f" : {str(P[-1])}" 
                fileE.write(f"{add} => {playerstat}\n")
    fileE.close()
    os.system('start leaders/Pitching_Leaders.txt')

def READHITTERS():
    try:
        bats = []
        lineasB = lines[lines.index('&&&&&\n') +1: lines.index('&&&&-\n')]
        for i in lineasB:
            i = i.replace("," , " ").replace("    ", " ").replace(";" , " ")
            i = i.split()
            bats.append(i)
        for i in bats:
            H = float(i[-9])
            BB = float(i[-8])
            HBP = float(i[-7])
            SF = float(i[-6])
            TB = float(i[-5])
            DOSB = float(i[-4])
            TRESB = float(i[-3])
            HR = float(i[-2])
            CI = float(i[-1])

            PRO = round((H / TB) *1000  )
            i.append(PRO)

            OBP = round( (H + BB + HBP) / (TB + BB + HBP + SF) , 3)
            i.append(OBP)

            SLG = round( ((H- DOSB - TRESB - HR) + (2*DOSB) + (3*TRESB) + (4*HR)) 
                        / TB , 3)
            i.append(SLG)
        return bats
    except IndexError:
        print("REVISA QUE EL ARCHIVO ESTE EN EL FOMATO CORRECTO")

def LIDSHITT(l):
    fileE = open('leaders/Batting_Leaders.txt' , 'w')
    equipos = READTEAMS()
    fileE.write("Batting  Leaders: \n\n")
    fileE.write("TOP 3 HITTERS BY HOME RUNS: \n")
    topHR = sorted(l , key=lambda x: float(x[-5]) ,reverse=True)
    for E in topHR[:3]:
        add = ""
        playerstat = ""
        IDHR = E[0]
        for i in range(0, len(equipos)):
            if IDHR == equipos[i][0]:
                for j in range(1 , len(teams[i]) - 5):
                    add += f"{str(teams[i][j])} "
                playerstat += f"{str(E[2])} " + f"{str(E[3])}" + f" : {str(E[-5])}"
                fileE.write(f"{add} =>  {playerstat}\n")
    fileE.write("\n")

    fileE.write("TOP 3 HITTERS BY HITS:\n")
    topH = sorted(l , key=lambda x: float(x[-12]) , reverse=True)
    for W in topH[:3]:
        add = ""
        playerstat = ""
        IDH = W[0]
        for w in range(0, len(equipos)):
            if IDH == equipos[w][0]:
                for j in range(1 , len(teams[i]) - 5):
                    add += f"{str(teams[w][j])} "
                playerstat += f"{str(W[2])} " + f"{str(W[3])}" + f" : {str(W[-12])}"
                fileE.write(f"{add} =>  {playerstat}\n")
    fileE.write("\n")

    fileE.write("TOP 3 HITS BY RBI:\n")
    topCI = sorted(l , key=lambda x: float(x[-4]) , reverse=True) 
    for C in topCI[:3]:
        add = ""
        playerstat = ""
        IDC = C[0]
        for c in range(0, len(equipos)):
            if IDC == equipos[c][0]:
                for j in range(1 , len(teams[c]) - 5):
                    add += f"{str(teams[c][j])} "
                playerstat += f"{str(C[2])} " + f"{str(C[3])}" + f" : {str(C[-4])}"
                fileE.write(f"{add} =>  {playerstat}\n")
    fileE.close()
    os.system('start leaders/Batting_Leaders.txt')

def READDEFENSES():
    try:
        defe = []
        lineasD = lines[lines.index('!!!!!\n')+1 :lines.index('!!!!-\n')]
        for i in lineasD:
            i = i.replace("," , " ").replace(":", " ").replace(";" , " ")
            i = i.split()
            defe.append(i)
        for i in defe:
            JJ = float(i[-5])
            O = float(i[-4])
            A = float(i[-3])
            E = float(i[-2])
            DP = float(i[-1])
            TL = O + A + E
            PF = round(((O + A) / TL) , 3)
            DPJ =round((DP / JJ) , 3)
            i.append(PF)
            i.append(TL)
            i.append(DPJ)
        return defe
    except IndexError:
        print("REVISA QUE EL ARCHIVO ESTE EN EL FOMATO CORRECTO")

def LIDSDEF(l):
    fileE = open('leaders/Defensive_Leaders.txt' , 'w')
    equipos = READTEAMS()
    fileE.write("Defense  Leaders: \n\n")
    fileE.write("TOP 3 DEFENSES BY PRECISION: \n")
    topE = sorted(l , key=lambda x: float(x[-5])) 
    for E in topE[:3]:
        add = ""
        playerstat = ""
        IDE = E[0]
        for e in range(0,len(equipos)):
            if IDE == equipos[e][0]:
                for j in range(1 , len(teams[e]) - 5):
                    add += f"{str(teams[e][j])} "
                playerstat += f"{str(E[2])} " + f"{str(E[3])}" + f" : {str(E[-5])}"
                fileE.write(f"{add} => {playerstat}\n")
    fileE.write("\n")

    fileE.write("TOP 3 DEFENSES BY F%: \n")
    topF = sorted(l , key=lambda x: x[-3] , reverse=True)
    for F in topF[:3]:
        add = ""
        playerstat = ""
        IDF = F[0]
        for w in range(0, len(equipos)):
            if IDF == equipos[w][0]:
                for j in range(1 , len(teams[w]) - 5):
                    add += f"{str(teams[w][j])} "
                playerstat += f"{str(F[2])} " + f"{str(F[3])}" + f" : {str(F[-3])}"
                fileE.write(f"{add} => {playerstat}\n")
    fileE.write("\n")

    fileE.write("TOP 3 DEFENSES BY DP/J: \n")
    topDPJ = sorted(l , key=lambda x: x[-1] , reverse=True)
    for P in topDPJ[:3]:
        add = ""
        playerstat = ""
        IDDPJ = P[0]
        for p in range(0, len(equipos)):
            if IDDPJ == equipos[p][0]:
                for j in range(1 , len(teams[p]) - 5):
                    add += f"{str(teams[p][j])} "
                playerstat += f"{str(P[2])} " + f"{str(P[3])}" + f" : {str(P[-1])}"
                fileE.write(f"{add} => {playerstat}\n")
    fileE.close()
    os.system('start leaders/Defensive_Leaders.txt')

teams = READTEAMS()
pitchers = READPITCHERS()
hitters = READHITTERS()
defenses = READDEFENSES()

def writeTeams():
    fileT = open('teams.txt', 'w')
    fileT.write("TEAMS LEADERBOARD\n\n")
    pos = 1
    for i in teams:
        add = ""
        for j in range(1 , len(i) - 5):
            add += f"{str(i[j])} "
        add += f" => DIF: {i[-1]}"
        fileT.write(f"{pos}- {add}  \n\n")
        pos +=1
    fileT.close()

#-------------------------------------------------------------------------------------------------------------------
app = Tk()
app.title("Stats Baseball")
app.geometry("1100x500")
app.iconbitmap("icon/iconAPP.ico")
app.resizable(False,False)
app.config(cursor="circle")
app.configure(background="gray")

def Save_value():
    ID = id.get()
    return ID

def destroy_frame_widgets():
    for widget in screen.winfo_children():
        widget.destroy()
def reset_frame():
    destroy_frame_widgets()
    screen.place(x=250 , y=100)

def leadersP():
    LIDSSPI(pitchers)

def leadersH():
    LIDSHITT(hitters)

def leadersD():
    LIDSDEF(defenses)
#PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
def Pitchers():
    reset_frame()
    global byLidsP
    byTP = Button(screen , text="By Teams" , command=Pbyteams , width=15 , border=5)
    byLidsP = Button(screen , text="Lids" , command=leadersP , width=15 , border=5)
    byTP.grid(row=0 , column=0)
    byLidsP.grid(row=0 , column=1)

def Pbyteams():
    global id
    global showP
    writeTeams()
    byLidsP.destroy()
    showP = scrolledtext.ScrolledText(screen, width=80, height=15 )
    showP.configure(font="Calibri 12")
    showP.grid(row=6 , column=1)
    for i in teams:
        add = "ID: "
        for j in range(0 , len(i) - 5):
            add += f"{str(i[j])} "
        showP.insert(END, f'{add}\n')
    table = Label(screen, justify="left",text="#    |    Name    |      Last Name     |     Pos    |   P   |     BB     |     H     |      IL     |     CL    |     EFE    |     WHIP    |    P/BB    |" , bg="white" , border=12)
    table.grid(row=5 , column=1)

    id = Entry(screen)
    id.insert(0 , "<ID of the team>")
    id.grid(row=1 , column=0)
    send = Button(screen ,text="Print" , command=ShowP , width=15 , border=5)
    send.grid(row=2 , column=0)

def ShowP():
    showP.delete("1.0", END)
    value = Save_value()
    add = ""
    for i in teams:
        if value == i[0]:
            for j in range(1,len(i) - 5):
                add += str(f"{i[j]} ")
            showP.insert(END , f"Team: {add} \n\n")
            break    
    for i in pitchers:
        add = ""
        if i[0] == value:
            for j in range(1,len(i)):
                add += str(f"{i[j]}    | ")
            showP.insert(END , f"{add} \n")

#HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
def Hitters():
    reset_frame()
    global byLidsH
    byTH = Button(screen , text="By Teams" , command=Hbyteams, width=15 , border=5)
    byLidsH = Button(screen , text="Lids" , command=leadersH , width=15 , border=5 )
    byTH.grid(row=0 , column=0)
    byLidsH.grid(row=0 , column=1)

def Hbyteams():
    global id
    global showH
    writeTeams()
    byLidsH.destroy()
    showH = scrolledtext.ScrolledText(screen,  width=80, height=15)
    showH.configure(font="Calibri 12")
    showH.grid(row=6 , column=1)
    for i in teams:
        add = "ID: "
        for j in range(0 , len(i) - 5):
            add += f"{str(i[j])} "
        showH.insert(END, f'{add}\n')
    table = Label(screen, text="#   |  Nom  |  Ape  | Pos |   H   |   BB   |   HBP   |   SF   |   TB  |   2B  |   3B  |   HR   |   CI  |    PRO   |    OBP   |   SLG" , bg="white" , border=12)
    table.grid(row=5 , column=1)

    id = Entry(screen)
    id.insert(0 , "<ID of the team>")
    id.grid(row=1 , column=0)
    send = Button(screen ,text="Print" , command=ShowH , width=15 , border=5)
    send.grid(row=2 , column=0)

def ShowH():
    showH.delete("1.0", END)
    value = Save_value()
    add = ""
    for i in teams:
        if value == i[0]:
            for j in range(1,len(i) - 5):
                add += str(f"{i[j]} ")
            showH.insert(END , f"Team: {add} \n\n")
            break    
    for i in hitters:
        add = ""
        if i[0] == value:
            for j in range(1,len(i)):
                add += str(f"{i[j]} | ")
            showH.insert(END , f"{add} \n")
#DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
def Defenses():
    reset_frame()
    global byLidsD
    byTD = Button(screen , text="By Teams" , command=Dbyteams, width=15 , border=5)
    byLidsD = Button(screen , text="Lids" , command=leadersD , width=15 , border=5 )
    byTD.grid(row=0 , column=0)
    byLidsD.grid(row=0 , column=1)

def Dbyteams():
    global id
    global showD
    writeTeams()
    byLidsD.destroy()
    showD = scrolledtext.ScrolledText(screen,  width=80, height=15)
    showD.configure(font="Calibri 12")
    showD.grid(row=6 , column=1)
    for i in teams:
        add = "ID: "
        for j in range(0 , len(i) - 5):
            add += f"{str(i[j])} "
        showD.insert(INSERT, f'{add}\n')
    table = Label(screen, text=" #  |    Nom    |    Ape    |     Pos    |        O       |         A       |         E       |       DP      |      F%      |      TL      |        DP/J      |        " , bg="white" , border=12)
    table.grid(row=5 , column=1)

    id = Entry(screen)
    id.insert(0 , "<ID of the team>")
    id.grid(row=1 , column=0)
    send = Button(screen ,text="Print" , command=ShowD , width=15 , border=5)
    send.grid(row=2 , column=0)

def ShowD():
    showD.delete("1.0", END)
    value = Save_value()
    add = ""
    for i in teams:
        if value == i[0]:
            for j in range(1,len(i) - 5):
                add += str(f"{i[j]} ")
            showD.insert(END , f"Team: {add} \n\n")
            break    
    for i in defenses:
        add = ""
        if i[0] == value:
            for j in range(1,len(i)):
                add += str(f"{i[j]}  |  ")
            showD.insert(END , f"{add} \n")

#TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
def ShowT():
    writeTeams()
    os.system('teams.txt')

#SIMULATION FUNCTIONS
def Simulation():
    reset_frame()
    global RandomBtn , ChooseBtn
    ChooseBtn = Button(screen , text="Choose Teams" , command=ChooseTeams, width=15 , border=5)
    ChooseBtn.grid(row=0 , column=0)
    RandomBtn = Button(screen , text="Random Teams" , command=RandomPlay, width=15 , border=5)
    RandomBtn.grid(row=0 , column=1)

def ChooseTeams():
    global t1 , t2 , showT
    RandomBtn.destroy()
    t1 = Entry(screen)
    t1.insert(0 , "<ID of the team 1>")
    t1.grid(row=1 , column=0)
    t2 = Entry(screen)
    t2.insert(0 , "<ID of the team 2>")
    t2.grid(row=2 , column=0)
    Play = Button(screen , text="Play" , command=PlayGame , width=15 , border=5)
    Play.grid(row=0 , column=1)

    writeTeams()
    showT = scrolledtext.ScrolledText(screen,  width=80, height=15)
    showT.configure(font="Calibri 12")
    showT.grid(row=6 , column=1)
    for i in teams:
        add = "ID: "
        for j in range(0 , len(i) - 5):
            add += f"{str(i[j])} "
        showT.insert(INSERT, f'{add}\n')

def RandomPlay():
    global t1, t2 , showT
    ChooseBtn.destroy()
    RandomBtn.grid(row=0,column=0)
    showT = scrolledtext.ScrolledText(screen,  width=80, height=15)
    showT.configure(font="Calibri 12")
    showT.grid(row=6 , column=1)
    Play = Button(screen , text="Play" , command=PlayGame , width=15 , border=5)
    Play.grid(row=0 , column=1)
    
    writeTeams()
    showT = scrolledtext.ScrolledText(screen,  width=80, height=15)
    showT.configure(font="Calibri 12")
    showT.grid(row=6 , column=1)
    for i in teams:
        add = ""
        for j in range(1 , len(i) - 5):
            add += f"{str(i[j])} "
        showT.insert(INSERT, f'{add}\n')
    
    t1 = Entry(screen)
    t2 = Entry(screen)
    random1 = str(random.randint(1,numE))
    random2 = str(random.randint(1,numE))
    while random1 == random2:
        random2 = str(random.randint(1,numE))
    t1.delete(0, END)
    t1.insert(0 , random1)
    t2.delete(0 , END)
    t2.insert(0 , random2)

def PlayGame():
    showT.delete("1.0" , END)
    team1 = t1.get()
    team2 = t2.get()
    nameTeam1 = ""
    nameTeam2 = ""
    averageOBPA = 0
    averageOBPB = 0
    averageEFEA = 0
    averageEFEB = 0
    averagePFA = 0
    averagePFB = 0
    OBPSA = 0
    OBPSB = 0
    EFEA = 0
    EFEB = 0
    PFA = 0
    PFB = 0
    pointsA = 0
    pointsB = 0
    for i in teams:
        if i[0] == team1:
            for j in range(1 , len(i) - 5):
                nameTeam1 += f"{str(i[j])} "
        elif i[0] == team2:
            for j in range(1 , len(i) - 5):
                nameTeam2 += f"{str(i[j])} "
    try:
        showT.insert(END , f"{nameTeam1} Vs {nameTeam2}\n-----------------------------------------------------------------\n")
    except UnboundLocalError:
        showT.insert(END , "No team was chosen.")
    for i in range(0,3):
        playersA = 0
        playersB = 0
        if i == 0:
            for i in hitters:
                if i[0] == team1:
                    OBPSA += i[-2]
                    playersA += 1
                elif i[0] == team2:
                    OBPSB += i[-2]
                    playersB += 1
            averageOBPA = round(OBPSA / playersA , 3)
            averageOBPB = round(OBPSB / playersB , 3)

            if averageOBPA > averageOBPB:
                pointsA += 1
            elif averageOBPB > averageOBPA:
                pointsB += 1
            showT.insert(END , "BETTER AVERAGE OBP\n")
            showT.insert(END , f"{nameTeam1}: {pointsA}\n")
            showT.insert(END , f"{nameTeam2}: {pointsB}")
            showT.insert(END , "\n")

        elif i == 1:
            for i in pitchers:
                if i[0] == team1:
                    EFEA += i[-3]
                    playersA += 1
                elif i[0] == team2:
                    EFEB += i[-3]
                    playersB += 1
            averageEFEA = round(EFEA / playersA , 2)
            averageEFEB = round(EFEB / playersA , 2)

            if averageEFEA > averageEFEB:
                pointsA += 1 
            elif averageEFEB > averageEFEA:
                pointsB += 1
            showT.insert(END , "\n")
            showT.insert(END , "BETTER AVERAGE EFE\n")
            showT.insert(END , f"{nameTeam1}: {pointsA}\n")
            showT.insert(END , f"{nameTeam2}: {pointsB}")    
            showT.insert(END , "\n")

        elif i == 2:
            for i in defenses:
                if i[0] == team1:
                    PFA += i[-3]
                    playersA += 1
                elif i[0] == team2:
                    PFB += i[-3]
                    playersB += 1
            averagePFA = round(PFA / playersA , 3)
            averagePFB = round(PFB / playersB , 3)
                        
            if averagePFA > averagePFB:
                pointsA += 1
            elif averagePFB > averagePFA:
                pointsB += 1
            showT.insert(END , "\n")
            showT.insert(END , "BETTER AVERAGE F%\n")
            showT.insert(END , f"{nameTeam1}: {pointsA}\n")
            showT.insert(END , f"{nameTeam2}: {pointsB}")
            showT.insert(END , "\n")
            if pointsA > pointsB:
                    showT.insert(END , f"WIN ==> {nameTeam1}")
            elif pointsB > pointsA:
                showT.insert(END , f"WIN ==> {nameTeam2}")
            else:
                showT.insert(END , "Draw?")
            print("\n")

title = Label(app, text="Baseball Stats", bg="gray" , font="Corbel 25" , pady=20)
title.pack()

Pbtn = Button(app , text="Pitchers" , command=Pitchers , width=15 , border=5)
Pbtn.pack(anchor="w" , padx="5px" , pady="10px")

Bbtn = Button(app ,text="Hitters" , command=Hitters , width=15 , border=5)
Bbtn.pack(anchor="w" , padx="5px" , pady="10px")

Dbtn = Button(app ,text="Defenses" , command=Defenses , width=15 , border=5)
Dbtn.pack(anchor="w" , padx="5px" , pady="10px")

Tbtn = Button(app ,text="Teams" , command=ShowT , width=15 , border=5)
Tbtn.pack(anchor="w" , padx="5px" , pady="10px")

Sbtn = Button(app ,text="Simulation" , command=Simulation , width=15 , border=5)
Sbtn.pack(anchor="w" , padx="5px" , pady="10px")

back = Button(app ,text="BACK" , command=reset_frame , width=15 , border=5)
back.pack(anchor="w" , padx="5px" , pady="10px")

screen = Frame(app, width=500, heigh=350, bg="gray")
screen.pack_propagate(False)
screen.place(x=250 , y=100)

app.mainloop()