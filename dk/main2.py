import csv
import json
import time

salary = 50000
sport = "football"
JSONDir = "DKDataConvertedToJSON/"
qbJSON = "qb.txt"
wrJSON = "wr.txt"
rbJSON = "rb.txt"
teJSON = "te.txt"
flexJSON = "flex.txt"
dstJSON = "dst.txt"

def computeData():
    
    
    with open(JSONDir + qbJSON) as json_file:  
        qbdata = json.load(json_file)
    with open(JSONDir + wrJSON) as json_file:  
        wrdata = json.load(json_file)
    with open(JSONDir + rbJSON) as json_file:  
        rbdata = json.load(json_file)
    with open(JSONDir + teJSON) as json_file:  
        tedata = json.load(json_file)
    with open(JSONDir + flexJSON) as json_file:  
        flexdata = json.load(json_file)
    with open(JSONDir + dstJSON) as json_file:  
        dstdata = json.load(json_file)
    print("starting")
    with open('results.csv', mode='w') as results:
        results = csv.writer(results, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for qb in qbdata['QB']:
            print("here")
            done = False
            count = 0
            currentSal = 0
            best = 0
            for a in range(len(rbdata['RB'])):
                if(count == 500000):
                    break
                currentSal = int(qb['salary'])+int(rbdata['RB'][a]['salary'])
                for b in range(len(rbdata['RB'])-1):
                    b=b+1
                    if(count == 500000):
                        break
                    currentSal = int(qb['salary']) + int(rbdata['RB'][a]['salary']) + int(rbdata['RB'][b]['salary'])
                    if(rbdata['RB'][a] != rbdata['RB'][b] and currentSal <= salary and done == False):
                        for c in range(len(wrdata['WR'])):
                            if(count == 500000):
                                break
                            for d in range(len(wrdata['WR'])-1):
                                d = d+1
                                if(count == 500000):
                                    break
                                time.sleep(1)
                                currentSal = int(qb['salary']) + int(rbdata['RB'][a]['salary']) + int(rbdata['RB'][b]['salary']) + int(wrdata['WR'][c]['salary']) + int(wrdata['WR'][d]['salary'])
                                if(wrdata['WR'][c] != wrdata['WR'][d] and currentSal <= salary and done == False):
                                    for e in range(len(wrdata['WR'])-2):
                                        e = e + 2
                                        if(count == 500000):
                                            break
                                        currentSal = int(qb['salary']) + int(rbdata['RB'][a]['salary']) + int(rbdata['RB'][b]['salary']) + int(wrdata['WR'][c]['salary']) + int(wrdata['WR'][d]['salary']) + int(wrdata['WR'][e]['salary'])
                                        if(wrdata['WR'][c] != wrdata['WR'][e] and wrdata['WR'][d] != wrdata['WR'][e] and currentSal <= salary and done == False):
                                            for te in tedata['TE']:
                                                if(count == 500000):
                                                    break
                                                currentSal = int(qb['salary']) + int(rbdata['RB'][a]['salary']) + int(rbdata['RB'][b]['salary']) + int(wrdata['WR'][c]['salary']) + int(wrdata['WR'][d]['salary']) + int(wrdata['WR'][e]['salary']) + int(te['salary'])
                                                if(currentSal <= salary and done == False):
                                                    for flex in flexdata['FLEX']:
                                                        if(count == 500000):
                                                            break
                                                        currentSal = int(qb['salary']) + int(rbdata['RB'][a]['salary']) + int(rbdata['RB'][b]['salary']) + int(wrdata['WR'][c]['salary']) + int(wrdata['WR'][d]['salary']) + int(wrdata['WR'][e]['salary']) + int(te['salary']) + int(flex['salary'])
                                                        if(flex != rbdata['RB'][a] and flex != rbdata['RB'][b] and flex != wrdata['WR'][c] and flex != wrdata['WR'][d] and flex != wrdata['WR'][e] and flex != te and currentSal <= salary and done == False):
                                                            for dst in dstdata['DST']:
                                                                if(count == 500000):
                                                                    break
                                                                currentSal = int(qb['salary']) + int(rbdata['RB'][a]['salary']) + int(rbdata['RB'][b]['salary']) + int(wrdata['WR'][c]['salary']) + int(wrdata['WR'][d]['salary']) + int(wrdata['WR'][e]['salary']) + int(te['salary']) + int(flex['salary']) + int(dst['salary'])
                                                                projscore = float(qb['projpoints']) + float(rbdata['RB'][a]['projpoints']) + float(rbdata['RB'][b]['projpoints']) + float(wrdata['WR'][c]['projpoints']) + float(wrdata['WR'][d]['projpoints']) + float(wrdata['WR'][e]['projpoints']) + float(te['projpoints']) + float(flex['projpoints']) + float(dst['projpoints'])
                                                                avgscore = float(qb['avgpoints']) + float(rbdata['RB'][a]['avgpoints']) + float(rbdata['RB'][b]['avgpoints']) + float(wrdata['WR'][c]['avgpoints']) + float(wrdata['WR'][d]['avgpoints']) + float(wrdata['WR'][e]['avgpoints']) + float(te['avgpoints']) + float(flex['avgpoints']) + float(dst['avgpoints'])
                                                                if(currentSal <= salary and done == False and projscore > best):
                                                                    best = projscore
                                                                    count=count+1
                                                                    print("found: " + str(count) + " QB: " + qb['name'])
                                                                    results.writerow([currentSal,projscore,avgscore,qb['name'] , rbdata['RB'][a]['name'], rbdata['RB'][b]['name'], wrdata['WR'][c]['name'],wrdata['WR'][d]['name'], wrdata['WR'][e]['name'], te['name'],flex['name'], dst['name']])
                                                                    if(count == 500000):
                                                                        break
                                                                    
            
    print("done.")

def main():
    
    computeData()
    


if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main()