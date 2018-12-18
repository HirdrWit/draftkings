#https://www.fantasypros.com/nfl/reports/leaders/?year=2018&start=1&end=7
#https://www.teamrankings.com/nfl/odds/
#http://www.borischen.co/p/quarterback-tier-rankings.html
#https://www.fantasypros.com/nfl/start/jameis-winston-tom-brady.php
import csv
import json
import time
import sys

gamedata = "/Users/hirro001/Desktop/pythonStuff/dk3/pbp-2018.csv"
playerdata = "/Users/hirro001/Desktop/pythonStuff/dk2/FantasyPros_Fantasy_Football_Points.csv"
spread = "/Users/hirro001/Desktop/pythonStuff/dk3/spread.csv"
def getData():
    players = []
    offData = {}
    defData = {}
    with open(gamedata) as csvfile:
        reader = csv.DictReader(csvfile)
        last_team = "none"
        for row in reader:
            Off = row['OffenseTeam']
            Def = row['DefenseTeam']
            description = row['Description']
            yards = row['Yards']
            play = row['PlayType']
            passtype = row['PassType']
            rushdir = row['RushDirection']
            touchdown = row['IsTouchdown']
            
            if(last_team != Off):
                players = []
                players = getPlayers(Off)
                last_team = Off

            if(play == "RUSH"):
                for player in players:
                    if(player in description):
                        offData = addOffData(Off, player, play, rushdir, yards, offData, touchdown)
                        defData = addDefData(Def, play, rushdir, yards,defData,touchdown)
                        #printDataForDebug(Off,description,player,play,rushdir,yards,touchdown)
                        break
            if(play == "PASS"):
                for player in players:
                    if(player in description):
                        offData = addOffData(Off, player, play, passtype, yards, offData,touchdown)
                        defData = addDefData(Def, play, passtype, yards,defData,touchdown)
                        #printDataForDebug(Off,description,player,play,passtype,yards,touchdown)
                        break
    return(offData,defData)

def printDataForDebug(Off,description,player,play,Dir,yards,touchdown):
    print(Off)
    print(description)
    print("Main Player: " + player)
    print("Play Type: " + play)
    print("Play Dir: " + Dir)
    print("Yards: "+ yards)
    print("Touchdown: "+ touchdown)
    print("\n")

def getNumPos(dir):
    yardpos = 100
    countpos = 100
    touchdown = 100
    if(dir == "LEFT END"):
        yardpos = 8
        countpos = 1
        touchdown = 27
    elif(dir == "LEFT TACKLE"):
        yardpos = 9
        countpos = 2
        touchdown = 28
    elif(dir == "LEFT GUARD"):
        yardpos = 10
        countpos = 3
        touchdown = 29
    elif(dir == "CENTER"):
        yardpos = 11
        countpos = 4
        touchdown = 30
    elif(dir == "RIGHT END"):
        yardpos = 12
        countpos = 5
        touchdown = 31
    elif(dir == "RIGHT TACKLE"):
        yardpos = 13
        countpos = 6
        touchdown = 32
    elif(dir == "RIGHT GUARD"):
        yardpos = 14
        countpos = 7
        touchdown = 33
    elif(dir == "SHORT LEFT"):
        yardpos = 21
        countpos = 15
        touchdown = 34
    elif(dir == "SHORT RIGHT"):
        yardpos = 22
        countpos = 16
        touchdown = 35
    elif(dir == "SHORT MIDDLE"):
        yardpos = 23
        countpos = 17
        touchdown = 36
    elif(dir == "DEEP LEFT"):
        yardpos = 24
        countpos = 18
        touchdown = 37
    elif(dir == "DEEP RIGHT"):
        yardpos = 25
        countpos = 19
        touchdown = 38
    elif(dir == "DEEP MIDDLE"):
        yardpos = 26
        countpos = 20
        touchdown = 39
    else:
        print("UNKNOWN CASE!!!")
        print(dir)
    return[yardpos,countpos,touchdown]


    #offData[player] = 
    # Off [0], rushLECount[1], rushLTCount[2], rushLGCount[3], rushCCount[4], rushRECount[5], rushRTCount[6], rushRGCount[7], 
    # rushLEYards[8], rushLTYards[9], rushLGYards[10], rushCYards[11], rushREYards[12], rushRTYards[13], rushRGYards[14], 
    # passSLCount[15], passSLCount[16], passSLCount[17], passSLCount[18], passSLCount[19], passSLCount[20], 
    # passSLYards[21], passSLYards[22], passSLYards[23], passSLYards[24], passSLYards[25], passSLYards[26] 

def addOffData(Off, player, play, dir, yards, offData,isTouchdown):
    if play != "INTERCEPTED BY":
        values = getNumPos(dir)
        yardpos = values[0]
        countpos = values[1]
        touchdownpos = values[2]

    if play == "INTERCEPTED BY":
        return offData
    #playerDic[row['Player']] = [row['Avg'], row['Games']]
    data = offData.get(player) 

    if(data==None) :
        offData[player] = [Off, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        data = offData.get(player) 
    
    offData[player][yardpos] += float(yards)
    offData[player][countpos] += 1
    if int(isTouchdown):
        #print("Adding touchdown to :" + player)
        offData[player][touchdownpos] += 1
    return offData
    
def addDefData(Def, play, dir, yards,defData, isTouchdown):
    if play != "INTERCEPTED BY":
        values = getNumPos(dir)
        yardpos = values[0] - 1
        countpos = values[1] - 1
        touchdownpos = values[2] - 1

    if play == "INTERCEPTED BY" or play == "NOT LISTED":
        return defData
    #playerDic[row['Player']] = [row['Avg'], row['Games']]
    data = defData.get(Def) 

    if(data==None) :
        defData[Def] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        data = defData.get(Def) 
    
    defData[Def][yardpos] += float(yards)
    defData[Def][countpos] += 1
    if int(isTouchdown):
        defData[Def][touchdownpos] += 1
    return defData

def getPlayers(team):
    players = []
    with open(playerdata) as csvfile:
        reader = csv.DictReader(csvfile)
        if(team == 'LA'):
            team = 'LAR'
        for row in reader:
            if(row['Position'] == 'WR' or row['Position'] == 'TE' or row['Position'] == 'RB'):
                if(row['Team'] == team):
                    #print(row['Player'])
                    p = row['Player'].split()[0][0]+"."+row['Player'].split()[1]
                    p = p.upper()
                    players.append(p)
        return players

def analyzeSpread(offData, defData):
    orig_stdout = sys.stdout
    f = open('out.txt', 'w')
    sys.stdout = f
    with open(spread) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:  
            team1 = row['Team1']
            team2 = row['Team2']
            teams = [team1,team2]
            for team in teams:
                print("Offense")
                for data in offData:
                    if(offData.get(data)[0] == team):
                        print(offData.get(data))
                            
                    # print("Player: " + data)
                    # print("Rushing Count")
                    # print("\tLeft End: " + str(offData.get(data)[1]))
                    # print("\tLeft Tackle: " + str(offData.get(data)[2]))
                    # print("\tLeft Guard: " + str(offData.get(data)[3]))
                    # print("\tCenter: " + str(offData.get(data)[4]))
                    # print("\tRight End: " + str(offData.get(data)[5]))
                    # print("\tRight Tackle: " + str(offData.get(data)[6]))
                    # print("\tRight Guard: " + str(offData.get(data)[7]))
                    # print("Rushing Yards")
                    # print("\tLeft End: " + str(offData.get(data)[8]))
                    # print("\tLeft Tackle: " + str(offData.get(data)[9]))
                    # print("\tLeft Guard: " + str(offData.get(data)[10]))
                    # print("\tCenter: " + str(offData.get(data)[11]))
                    # print("\tRight End: " + str(offData.get(data)[12]))
                    # print("\tRight Tackle: " + str(offData.get(data)[12]))
                    # print("\tRight Guard: " + str(offData.get(data)[12]))
                    # print("Rushing Touchdowns")
                    # print("\tLeft End: " + str(offData.get(data)[27]))
                    # print("\tLeft Tackle: " + str(offData.get(data)[28]))
                    # print("\tLeft Guard: " + str(offData.get(data)[29]))
                    # print("\tCenter: " + str(offData.get(data)[30]))
                    # print("\tRight End: " + str(offData.get(data)[31]))
                    # print("\tRight Tackle: " + str(offData.get(data)[32]))
                    # print("\tRight Guard: " + str(offData.get(data)[33]))
                    # print("Pass Count")
                    # print("\tShort Left: " + str(offData.get(data)[15]))
                    # print("\tShort Right: " + str(offData.get(data)[16]))
                    # print("\tShort Middle: " + str(offData.get(data)[17]))
                    # print("\tDeep Left: " + str(offData.get(data)[18]))
                    # print("\tDeep Right: " + str(offData.get(data)[19]))
                    # print("Pass Yards")
                    # print("\tShort Left: " + str(offData.get(data)[21]))
                    # print("\tShort Right: " + str(offData.get(data)[22]))
                    # print("\tShort Middle: " + str(offData.get(data)[23]))
                    # print("\tDeep Left: " + str(offData.get(data)[24]))
                    # print("\tDeep Right: " + str(offData.get(data)[25]))
                    # print("Pass Touchdowns")
                    # print("\tShort Left: " + str(offData.get(data)[34]))
                    # print("\tShort Right: " + str(offData.get(data)[35]))
                    # print("\tShort Middle: " + str(offData.get(data)[36]))
                    # print("\tDeep Left: " + str(offData.get(data)[37]))
                    # print("\tDeep Right: " + str(offData.get(data)[38]))
    sys.stdout = orig_stdout
    f.close()
def getAverageOffData(data):
    temp = ['val',0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    try:
        temp[8] = data[8]/data[1]
    except ZeroDivisionError:
        temp[8] = 0
    try:
        temp[9] = data[9]/data[2]
    except ZeroDivisionError:
        temp[9] = 0
    try:
        temp[10] = data[10]/data[3]
    except ZeroDivisionError:
        temp[10] = 0
    try:
        temp[11] = data[11]/data[4]
    except ZeroDivisionError:
        temp[11] = 0
    try:
        temp[12] = data[12]/data[5]
    except ZeroDivisionError:
        temp[12] = 0
    try:
        temp[13] = data[13]/data[6]
    except ZeroDivisionError:
        temp[13] = 0
    try:
        temp[14] = data[14]/data[7]
    except ZeroDivisionError:
        temp[14] = 0
    try:
        temp[21] = data[21]/data[15]
    except ZeroDivisionError:
        temp[21] = 0
    try:
        temp[22] = data[22]/data[16]
    except ZeroDivisionError:
        temp[22] = 0
    try:
        temp[23] = data[23]/data[17]
    except ZeroDivisionError:
        temp[23] = 0
    try:
        temp[24] = data[24]/data[18]
    except ZeroDivisionError:
        temp[24] = 0
    try:
        temp[25] = data[25]/data[19]
    except ZeroDivisionError:
        temp[25] = 0
    try:
        temp[26] = data[26]/data[20]
    except ZeroDivisionError:
        temp[26] = 0
   
    return temp

def printGood(avgdata,data,val):
    if(8 in val or data[27]>3):
        print("Left End")
        print("\tTotal: " + str(data[8]) + " Avg: " + str(avgdata[8]) + " # of time ran: " + str(data[1]) + " # of touchdowns: " + str(data[27]))
    if(9 in val or data[28]>3):
        print("Left Tackle")
        print("\tTotal: " + str(data[9]) + " Avg: " + str(avgdata[9]) + " # of time ran: " + str(data[2]) + " # of touchdowns: " + str(data[28]))
    if(10 in val or data[29]>3):
        print("Left Gaurd")
        print("\tTotal: " + str(data[10]) + " Avg: " + str(avgdata[10]) + " # of time ran: " + str(data[3]) + " # of touchdowns: " + str(data[29]))
    if(11 in val or data[30]>3):
        print("Center")
        print("\tTotal: " + str(data[11]) + " Avg: " + str(avgdata[11]) + " # of time ran: " + str(data[4]) + " # of touchdowns: " + str(data[30]))
    if(12 in val or data[31]>3):
        print("Right End")
        print("\tTotal: " + str(data[12]) + " Avg: " + str(avgdata[12]) + " # of time ran: " + str(data[5]) + " # of touchdowns: " + str(data[31]))
    if(13 in val or data[32]>3):
        print("Right Tackle")
        print("\tTotal: " + str(data[13]) + " Avg: " + str(avgdata[13]) + " # of time ran: " + str(data[6]) + " # of touchdowns: " + str(data[32]))
    if(14 in val or data[33]>3):
        print("Right Guard")
        print("\tTotal: " + str(data[14]) + " Avg: " + str(avgdata[14]) + " # of time ran: " + str(data[7]) + " # of touchdowns: " + str(data[33]))
    if(21 in val or data[34]>3):
        print("Short Left")
        print("\tTotal: " + str(data[21]) + " Avg: " + str(avgdata[21]) + " # of time ran: " + str(data[15]) + " # of touchdowns: " + str(data[34]))
    if(22 in val or data[35]>3):
        print("Short Right")
        print("\tTotal: " + str(data[22]) + " Avg: " + str(avgdata[22]) + " # of time ran: " + str(data[16]) + " # of touchdowns: " + str(data[35]))
    if(23 in val or data[36]>3):
        print("Short Middle")
        print("\tTotal: " + str(data[23]) + " Avg: " + str(avgdata[23]) + " # of time ran: " + str(data[17]) + " # of touchdowns: " + str(data[36]))
    if(24 in val or data[37]>3):
        print("Deep Left")
        print("\tTotal: " + str(data[24]) + " Avg: " + str(avgdata[24]) + " # of time ran: " + str(data[18]) + " # of touchdowns: " + str(data[37]))
    if(25 in val or data[38]>3):
        print("Deep Right")
        print("\tTotal: " + str(data[25]) + " Avg: " + str(avgdata[25]) + " # of time ran: " + str(data[19]) + " # of touchdowns: " + str(data[38]))
    if(26 in val or data[39]>3):
        print("Deep Middle")
        print("\tTotal: " + str(data[26]) + " Avg: " + str(avgdata[26]) + " # of time ran: " + str(data[20])+ " # of touchdowns: " + str(data[39]))
def getAverageDefData(data):
    temp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    try:
        temp[7] = data[7]/data[0]
    except ZeroDivisionError:
        temp[7] = 0
    try:
        temp[8] = data[8]/data[1]
    except ZeroDivisionError:
        temp[8] = 0
    try:
        temp[9] = data[9]/data[2]
    except ZeroDivisionError:
        temp[9] = 0
    try:
        temp[10] = data[10]/data[3]
    except ZeroDivisionError:
        temp[10] = 0
    try:
        temp[11] = data[11]/data[4]
    except ZeroDivisionError:
        temp[11] = 0
    try:
        temp[12] = data[12]/data[5]
    except ZeroDivisionError:
        temp[12] = 0
    try:
        temp[13] = data[13]/data[6]
    except ZeroDivisionError:
        temp[13] = 0
    try:
        temp[20] = data[20]/data[14]
    except ZeroDivisionError:
        temp[20] = 0
    try:
        temp[21] = data[21]/data[15]
    except ZeroDivisionError:
        temp[21] = 0
    try:
        temp[22] = data[22]/data[16]
    except ZeroDivisionError:
        temp[22] = 0
    try:
        temp[23] = data[23]/data[17]
    except ZeroDivisionError:
        temp[23] = 0
    try:
        temp[24] = data[24]/data[18]
    except ZeroDivisionError:
        temp[24] = 0
    try:
        temp[25] = data[25]/data[19]
    except ZeroDivisionError:
        temp[25] = 0
    
   
    return temp

def printPoor(old,data,val):
    print("Weak Spots")
    if(val[0]== 7 or val[1]== 7 or val[2]== 7 or val[3]== 7 or old[26] >5):
        print("Left End")
        print("\tTotal Yards: " + str(old[7])+" Avg Yards: " + str(data[7])+ " # of time ran: " + str(old[0]) + " # of touchdowns: " + str(old[26]))
    if(val[0]== 8 or val[1]== 8 or val[2]== 8 or val[3]== 8 or old[27] >5):
        print("Left Tackle")
        print("\tTotal Yards: " + str(old[8])+" Avg Yards: " + str(data[8])+ " # of time ran: " + str(old[1]) + " # of touchdowns: " + str(old[27]))
    if(val[0]== 9 or val[1]== 9 or val[2]== 9 or val[3]== 9 or old[28] >5) :
        print("Left Gaurd")
        print("\tTotal Yards: " + str(old[9])+" Avg Yards: " + str(data[9])+ " # of time ran: " + str(old[2]) + " # of touchdowns: " + str(old[28]))
    if(val[0]== 10 or val[1]== 10 or val[2]== 10 or val[3]== 10 or old[29] >5):
        print("Center")
        print("\tTotal Yards: " + str(old[10])+" Avg Yards: " + str(data[10])+ " # of time ran: " + str(old[3]) + " # of touchdowns: " + str(old[29]))
    if(val[0]== 11 or val[1]== 11 or val[2]== 11 or val[3]== 11 or old[30] >5):
        print("Right End")
        print("\tTotal Yards: " + str(old[11])+" Avg Yards: " + str(data[11])+ " # of time ran: " + str(old[4]) + " # of touchdowns: " + str(old[30]))
    if(val[0]== 12 or val[1]== 12 or val[2]== 12 or val[3]== 12 or old[31] >5):
        print("Right Tackle")
        print("\tTotal Yards: " + str(old[12])+" Avg Yards: " + str(data[12])+ " # of time ran: " + str(old[5]) + " # of touchdowns: " + str(old[31]))
    if(val[0]== 13 or val[1]== 13 or val[2]== 13 or val[3]== 13 or old[32] >5):
        print("Right Guard")
        print("\tTotal Yards: " + str(old[13])+" Avg Yards: " + str(data[13])+ " # of time ran: " + str(old[6]) + " # of touchdowns: " + str(old[32]))
    if(val[0]== 20 or val[1]== 20 or val[2]== 20 or val[3]== 20 or old[33] >5):
        print("Short Left")
        print("\tTotal Yards: " + str(old[20])+" Avg Yards: " + str(data[20])+ " # of time ran: " + str(old[14]) + " # of touchdowns: " + str(old[33]))
    if(val[0]== 21 or val[1]== 21 or val[2]== 21 or val[3]== 21 or old[34] >5):
        print("Short Right")
        print("\tTotal Yards: " + str(old[21])+" Avg Yards: " + str(data[21])+ " # of time ran: " + str(old[15]) + " # of touchdowns: " + str(old[34]))
    if(val[0]== 22 or val[1]== 22 or val[2]== 22 or val[3]== 22 or old[35] >5):
        print("Short Middle")
        print("\tTotal Yards: " + str(old[22])+" Avg Yards: " + str(data[22])+ " # of time ran: " + str(old[16]) + " # of touchdowns: " + str(old[35]))
    if(val[0]== 23 or val[1]== 23 or val[2]== 23 or val[3]== 23 or old[36] >5):
        print("Deep Left")
        print("\tTotal Yards: " + str(old[23])+" Avg Yards: " + str(data[23])+ " # of time ran: " + str(old[17]) + " # of touchdowns: " + str(old[36]))
    if(val[0]== 24 or val[1]== 24 or val[2]== 24 or val[3]== 24 or old[37] >5):
        print("Deep Right")
        print("\tTotal Yards: " + str(old[24])+" Avg Yards: " + str(data[24])+ " # of time ran: " + str(old[18]) + " # of touchdowns: " + str(old[37]))
    if(val[0]== 25 or val[1]== 25 or val[2]== 25 or val[3]== 25 or old[38] >5):
        print("Deep Middle")
        print("\tTotal Yards: " + str(old[25])+" Avg Yards: " + str(data[25])+ " # of time ran: " + str(old[19]) + " # of touchdowns: " + str(old[38]))

def getPoorStats(data):
    temp = getAverageDefData(data)
    val = (sorted(range(len(temp)), key=lambda i: temp[i])[-4:])
    printPoor(data,temp,val)
    return val #every value needs to be +1

def getGoodStats(data, offval):
    temp = getAverageOffData(data)
    printGood(temp,data,offval)

def analyzeSpread2(offData, defData):
    with open(spread) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:  
            team1 = row['Team1']
            team2 = row['Team2']
            
            print(team1 + " Defense")
            val = getPoorStats(defData.get(team1))
            offval = [x+1 for x in val]
            print(team2 + " Offense")
            for player in offData:
                if(offData.get(player)[0] == team2):
                    print(player)
                    getGoodStats(offData.get(player), offval)

            print(team2 + " Defense")
            val = getPoorStats(defData.get(team2))
            offval = [x+1 for x in val]
            print(team1 + " Offense")
            for player in offData:
                if(offData.get(player)[0] == team1):
                    print(player)
                    getGoodStats(offData.get(player), offval)
            print("________________________________________________________\n")

def main():
    orig_stdout = sys.stdout
    f = open('out.txt', 'w')
    sys.stdout = f
    offData, defData = getData()
    analyzeSpread2(offData, defData)
    sys.stdout = orig_stdout
    f.close()

if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main()