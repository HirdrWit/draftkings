from bs4 import BeautifulSoup
import requests
import csv
import lxml
import time
import sys
import os

def join():
    with open('data_set.csv', mode='w' , newline='') as csv_file:
            p_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            p_writer.writerow(['Week','Year','GID','Name','Pos','Team','h/a','Oppt','DK points','DK salary','Temp','Weather','Wind'])

    script_dir = os.path.dirname(__file__)  

    weather = []
    with open(os.path.join(script_dir, '../weather.csv')) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            weather.append(row)

    with open(os.path.join(script_dir, '../rotoguru.csv')) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            week = row[0]
            year = row[1]
            team = row[5]

            for report in weather:
                week_bool = False
                year_bool = False
                team_bool = False
                w_week = report[1]
                w_year = report[0]
                w_team1 = report[2]
                w_team2 = report[3]
                # print(week + " " + year + " " + team)
                # print(w_week + " " + w_year + " " + w_team1 + " " + w_team2)
                # print("_____")
                if(week == w_week):
                    week_bool = True
                if(year == w_year):
                    year_bool = True
                if(team == w_team1 or team == w_team2):
                    team_bool = True
                if(team_bool and week_bool and year_bool):
                    with open('data_set.csv', mode='a' , newline='') as csv_file:
                        p_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        if(report[5] == 'DOME'):
                            report[6] = '0m'
                        p_writer.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],report[4],report[5], report[6]])
                    # print(row)
                    # print(report)
                    # print("____")
                    break

            # Week,Year,GID,Name,Pos,Team,h/a,Oppt
            # Year,Week,Away,Home


            
    
    
if __name__== "__main__":
  main()
