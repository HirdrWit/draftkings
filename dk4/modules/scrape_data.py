from bs4 import BeautifulSoup
import requests
import csv
import lxml
import time

def get_data():
    with open('rotoguru.csv', mode='w' , newline='') as csv_file:
            p_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            p_writer.writerow(['Week','Year','GID','Name','Pos','Team','h/a','Oppt','DK points','DK salary'])

    years = ['2018', '2017', '2016', '2015', '2014']
    weeks =['17', '16', '15', '14', '13', '12', '11', '10', '9', '8', '7', '6', '5', '4', '3', '2', '1']
    teams = []
    for year in years:
        for week in weeks:
            page = requests.get('http://rotoguru1.com/cgi-bin/fyday.pl?week='+week+'&year='+year+'&game=dk&scsv=1')
            soup = BeautifulSoup(page.text, 'html.parser')

            x = soup.find('pre')
            x = str(x)
            x = x.split("\n")

            for i in range(1,len(x)-1):
                
                y = x[i].split(";")
                y[3] = y[3].replace(",","")

                if(y[5] == 'buf'):
                    y[5] = 'Bills'
                if(y[5] == 'dal'):
                    y[5] = 'Cowboys'
                if(y[5] == 'tam'):
                    y[5] = 'Buccaneers'
                if(y[5] == 'atl'):
                    y[5] = 'Falcons'
                if(y[5] == 'bal'):
                    y[5] = 'Ravens'
                if(y[5] == 'cle'):
                    y[5] = 'Browns'
                if(y[5] == 'nwe'):
                    y[5] = 'Patriots'
                if(y[5] == 'car'):
                    y[5] = 'Panthers'
                if(y[5] == 'ind'):
                    y[5] = 'Colts'
                if(y[5] == 'lar'):
                    y[5] = 'Rams'
                if(y[5] == 'nyg'):
                    y[5] = 'Giants'
                if(y[5] == 'sfo'):
                    y[5] = '49ers'
                if(y[5] == 'hou'):
                    y[5] = 'Texans'
                if(y[5] == 'det'):
                    y[5] = 'Lions'
                if(y[5] == 'kan'):
                    y[5] = 'Chiefs'
                if(y[5] == 'phi'):
                    y[5] = 'Eagles'
                if(y[5] == 'pit'):
                    y[5] = 'Steelers'
                if(y[5] == 'den'):
                    y[5] = 'Broncos'
                if(y[5] == 'mia'):
                    y[5] = 'Dolphins'
                if(y[5] == 'chi'):
                    y[5] = 'Bears'
                if(y[5] == 'min'):
                    y[5] = 'Vikings'
                if(y[5] == 'lac'):
                    y[5] = 'Chargers'
                if(y[5] == 'nor'):
                    y[5] = 'Saints'
                if(y[5] == 'sea'):
                    y[5] = 'Seahawks'
                if(y[5] == 'ten'):
                    y[5] = 'Titans'
                if(y[5] == 'nyj'):
                    y[5] = 'Jets'
                if(y[5] == 'gnb'):
                    y[5] = 'Packers'
                if(y[5] == 'ari'):
                    y[5] = 'Cardinals'
                if(y[5] == 'cin'):
                    y[5] = 'Bengals'
                if(y[5] == 'jac'):
                    y[5] = 'Jaguars'
                if(y[5] == 'was'):
                    y[5] = 'Redskins'
                if(y[5] == 'sdg'):
                    y[5] = 'Chargers'
                if(y[5] == 'stl'):
                    y[5] = 'Rams'
                if(y[5] == 'oak'):
                    y[5] = 'Steelers'

                if(y[7] == 'buf'):
                    y[7] = 'Bills'
                if(y[7] == 'dal'):
                    y[7] = 'Cowboys'
                if(y[7] == 'tam'):
                    y[7] = 'Buccaneers'
                if(y[7] == 'atl'):
                    y[7] = 'Falcons'
                if(y[7] == 'bal'):
                    y[7] = 'Ravens'
                if(y[7] == 'cle'):
                    y[7] = 'Browns'
                if(y[7] == 'nwe'):
                    y[7] = 'Patriots'
                if(y[7] == 'car'):
                    y[7] = 'Panthers'
                if(y[7] == 'ind'):
                    y[7] = 'Colts'
                if(y[7] == 'lar'):
                    y[7] = 'Rams'
                if(y[7] == 'nyg'):
                    y[7] = 'Giants'
                if(y[7] == 'sfo'):
                    y[7] = '49ers'
                if(y[7] == 'hou'):
                    y[7] = 'Texans'
                if(y[7] == 'det'):
                    y[7] = 'Lions'
                if(y[7] == 'kan'):
                    y[7] = 'Chiefs'
                if(y[7] == 'phi'):
                    y[7] = 'Eagles'
                if(y[7] == 'pit'):
                    y[7] = 'Steelers'
                if(y[7] == 'den'):
                    y[7] = 'Broncos'
                if(y[7] == 'mia'):
                    y[7] = 'Dolphins'
                if(y[7] == 'chi'):
                    y[7] = 'Bears'
                if(y[7] == 'min'):
                    y[7] = 'Vikings'
                if(y[7] == 'lac'):
                    y[7] = 'Chargers'
                if(y[7] == 'nor'):
                    y[7] = 'Saints'
                if(y[7] == 'sea'):
                    y[7] = 'Seahawks'
                if(y[7] == 'ten'):
                    y[7] = 'Titans'
                if(y[7] == 'nyj'):
                    y[7] = 'Jets'
                if(y[7] == 'gnb'):
                    y[7] = 'Packers'
                if(y[7] == 'ari'):
                    y[7] = 'Cardinals'
                if(y[7] == 'cin'):
                    y[7] = 'Bengals'
                if(y[7] == 'jac'):
                    y[7] = 'Jaguars'
                if(y[7] == 'was'):
                    y[7] = 'Redskins'
                if(y[7] == 'sdg'):
                    y[7] = 'Chargers'
                if(y[7] == 'stl'):
                    y[7] = 'Rams'
                if(y[7] == 'oak'):
                    y[7] = 'Steelers'

        

                with open('rotoguru.csv', mode='a' , newline='') as csv_file:
                    p_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    p_writer.writerow([y[0],y[1],y[2],y[3],y[4],y[5],y[6],y[7],y[8],y[9]])
    #             if(y[5] not in teams):
    #                 teams.append(y[5])
    # print(teams)
        
def get_weather():
    with open('weather.csv', mode='w' , newline='') as csv_file:
            p_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            p_writer.writerow(['Year','Week','Away','Home','Temp','Weather','Wind'])

    years = ['2018', '2017', '2016', '2015', '2014']
    weeks =['17', '16', '15', '14', '13', '12', '11', '10', '9', '8', '7', '6', '5', '4', '3', '2', '1']
    teams = []
    for year in years:
        for week in weeks:
            page = requests.get('http://www.nflweather.com/en/week/'+year+'/week-'+week)
            soup = BeautifulSoup(page.text, 'html.parser')

            tbody = soup.find('tbody')
            tr = tbody.find_all('tr')
            for elem in tr:
                a_tag = elem.find_all('a')
                team1 = ""
                team2 = ""
                temp = ""
                weather = ""
                wind = ""
                for i in range(0,len(a_tag)):
                    temp = str(a_tag[i]).split(">")
                    temp[1] = temp[1].replace("</a","")
                    if(i == 0):
                        team1 = temp[1]
                    if(i == 3):
                        team2 = temp[1]
                
                td = elem.find_all('td')

                for i in range(0,len(td)):                   
                    if(i == 9):
                        weather_temp = str(td[i]).split(">")
                        weather_temp[1] = weather_temp[1].replace("</td","")
                        weather_temp[1] = weather_temp[1].replace("                  ","")
                        weather_val = weather_temp[1].split("f")
                        if(len(weather_val)> 1):
                            weather_temp = weather_val[0]
                            weather = weather_val[1] 
                        else:
                            weather_temp = '70'
                            weather = weather_val[0][0:-1]
                    if(i == 11):
                        wind_temp = str(td[i]).split(">")
                        wind_temp[1] = wind_temp[1].replace("</td","")     
                        wind = wind_temp[1]     
                weather = weather.replace("\n","")[1:]
                weather = weather.replace("              ","")
                with open('weather.csv', mode='a' , newline='') as csv_file:
                    p_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    p_writer.writerow([year,week,team1,team2,weather_temp.replace("\n",""),weather,wind])
    #             if(team1 not in teams):
    #                 teams.append(team1)
    # print(teams)
if __name__== "__main__":
  main()
