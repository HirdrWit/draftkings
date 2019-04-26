#https://www.fantasypros.com/nfl/reports/leaders/?year=2018&start=1&end=7
#https://www.teamrankings.com/nfl/odds/
#http://www.borischen.co/p/quarterback-tier-rankings.html
#https://www.fantasypros.com/nfl/start/jameis-winston-tom-brady.php
import csv
import json
import time

performanceData = "/Users/hirro001/Desktop/pythonStuff/dk2/FantasyPros_Fantasy_Football_Points.csv"
draftkingsData = "/Users/hirro001/Desktop/pythonStuff/dk2/DKSalaries.csv"
joinedData = "/Users/hirro001/Desktop/pythonStuff/dk2/joined_player_data.csv"
spread = "/Users/hirro001/Desktop/pythonStuff/dk2/spread.csv"


def joinPlayerData():
    playerDic = {}
    with open(performanceData) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            playerDic[row['Player']] = [row['Avg'], row['Games']]
    
    with open('joined_player_data.csv', mode='w') as csv_file:
        p_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        p_writer.writerow(['Name','Position','Team','GamesPlayed','AveragePoints','Salary','DKProjected','CostPerPoint'])
        with open(draftkingsData) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                p = playerDic.get(row['Name'])
                if p != None:
                    pName = row['Name']
                    pPos = row['Position']
                    pTeam = row['TeamAbbrev']
                    pGamesPlayed = p[1]
                    pAvg = p[0]
                    pSalary = row['Salary']
                    pProjected = row['AvgPointsPerGame']
                    if(float(pAvg) != 0):
                        pCostPerPoint = float(pSalary)/float(pAvg)
                    else:
                        pCostPerPoint = "NoN"
                    p_writer.writerow([pName,pPos,pTeam,pGamesPlayed,pAvg,pSalary,pProjected,str(pCostPerPoint)])
                
    
def printTeamsPlaying():
    s = set()
    with open(draftkingsData) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            s.add(row['Game Info'])
    for game in s:
        print(game)

def getPlayers(pos, team):
    print("potential %s"%(pos))
    with open(joinedData) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if(row['Position'] == pos and row['Team'] == team):
                if(float(row['DKProjected'])>=0):
                    print(row)
    
def printAnalyzeSpread(hmlScoring, basSpread,row):          
#ideal print message 
#TeamsVS is a X scoring game
    print("Game %s is a %s point scoring game, this is %s scoring and the spread is %s"%(row['MatchUp'],row['Expected_Score'],hmlScoring,basSpread))
#Team X is projected to win by Y points
    print("Team %s is projected to win by %s points"%(row['Team1'],(row['Proj'])))
#if margin is big
    if(basSpread == "Big"):
    #You should draft running backs from winning team
        print("You should draft running backs from team %s"%(row['Team1']))
        #display running backs
        print("---RB---")
        getPlayers("RB",row['Team1'])
        print("You should draft WR from team %s"%(row['Team2']))
        #display running backs
        print("---WR---")
        getPlayers("WR",row['Team2'])
#if margin is close and high scoring
    if(basSpread == "Small" and hmlScoring == "High"):
    #You should draft QB, TE and WR from winning team
        print("You should draft QB, TE, and WR from %s"%(row['Team1']))
        #display QB
        print("---QB---")
        getPlayers("QB",row['Team1'])
        #display TE
        print("---TE---")
        getPlayers("TE",row['Team1'])
        #display WB
        print("---WR---")
        getPlayers("WR",row['Team1'])
    #Other Team Too
        print("You should draft QB, TE, and WR from %s"%(row['Team2']))
        #display QB
        print("---QB---")
        getPlayers("QB",row['Team2'])
        #display TE
        print("---TE---")
        getPlayers("TE",row['Team2'])
        #display WB
        print("---WR---")
        getPlayers("WR",row['Team2']) 
#if margin is close and medium scoring
    if(basSpread == "Small" and hmlScoring == "Medium"):
    #You should draft WR and TE from either team
        print("You should draft WR and TE from %s"%(row['Team1']))
        #display WR
        print("---WR---")
        getPlayers("WR",row['Team1'])
        #display TE
        print("---TE---")
        getPlayers("TE",row['Team1'])
        print("You should draft WR and TE from %s"%(row['Team2']))
        #display WR
        print("---WR---")
        getPlayers("WR",row['Team2'])
        #display TE
        print("---TE---")
        getPlayers("TE",row['Team2'])
#if margin is big and low scoring
    if(basSpread == "Big" and hmlScoring == "Low"):
    #You should draft DST from winning team
        print("You should draft the %s DST"%(row['Team1']))
        #display DST
#if low scoring
    if(hmlScoring == "Low" and basSpread == "Small"):
        print("It is not recommended to draft players from these teams, DST may have value")
        print("---WR---")
        getPlayers("WR",row['Team1'])
        print("---RB---")
        getPlayers("RB",row['Team1'])
        print("---WR---")
        getPlayers("WR",row['Team2'])
        print("---RB---")
        getPlayers("RB",row['Team2'])
    if(basSpread == "Average" and hmlScoring =="High"):
        print("You should draft running backs from team %s"%(row['Team1']))
        #display running backs
        print("---RB---")
        getPlayers("RB",row['Team1'])
        print("You should draft WR from team %s"%(row['Team1']))
        #display running backs
        print("---WR---")
        getPlayers("WR",row['Team1'])
        print("You should draft running backs from team %s"%(row['Team2']))
        #display running backs
        print("---RB---")
        getPlayers("RB",row['Team2'])
        print("You should draft WR from team %s"%(row['Team2']))
        #display running backs
        print("---WR---")
        getPlayers("WR",row['Team2'])
    if(basSpread == "Average" and hmlScoring =="Medium"):
        print("You should draft quarter backs from team %s"%(row['Team1']))
        #display running backs
        print("---QB---")
        getPlayers("QB",row['Team1'])
        print("You should draft quarter backs from team %s"%(row['Team2']))
        #display running backs
        print("---QB---")
        getPlayers("QB",row['Team2'])
        
    print("\n-------------")

def analyzeSpread():
    count = 0
    scoringRank = ["High","Medium","Low"]
    with open(spread) as csvfile:
        reader = csv.DictReader(csvfile)
        num_rows = sum(1 for row in csv.reader( open(spread))) - 1
        div = num_rows/3
        for row in reader:
            count = count + 1
            if(count <= div): hml = "High"
            elif(count <= 2*div): hml = "Medium"
            else: hml = "Low"
            if(float(row["Proj"])>6.5): bas = "Big"
            elif(float(row["Proj"])<=6.5 and float(row["Proj"])>3.5): bas = "Average"
            elif(float(row["Proj"])<=3.5): bas = "Small"

            printAnalyzeSpread(hml, bas, row,)
def findMissingPlayersInJoin():
    playerDic = {}
    with open(performanceData) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            playerDic[row['Player']] = [row['Avg'], row['Games']]
    with open('joined_player_data.csv', mode='w') as csv_file:
        p_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        p_writer.writerow(['Name','Position','Team','GamesPlayed','AveragePoints','Salary','DKProjected','CostPerPoint'])
        with open(draftkingsData) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                p = playerDic.get(row['Name']) 
                if(p==None) :
                    print(row['Name'])

def main():
    #joinPlayerData()
    #printTeamsPlaying()
    #findMissingPlayersInJoin()
    #analyzeSpread()
    
    with open(joinedData) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
             
            if(row['Name'] == 'Cole Beasley') :
                print(row)



if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main()