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

def loadData():
    rb,wr,qb,te,dst,flex = ({} for i in range(6)) 
    rb['RB'],wr['WR'],qb['QB'],te['TE'],dst['DST'],flex['FLEX']  = ([] for i in range(6))
    
    with open('/Users/hirro001/Desktop/pythonStuff/dk/RawDraftKingData/Book2.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if(row['position'] == 'RB'):
                rb['RB'].append({
                    'name': row['name'],
                    'salary':row['cost'],
                    'avgpoints':row['avg'],
                    'projpoints':row['proj']
                })
                flex['FLEX'].append({
                    'name': row['name'],
                    'salary':row['cost'],
                    'avgpoints':row['avg'],
                    'projpoints':row['proj']
                })
            elif(row['Position'] == 'WR') :
                wr['WR'].append({
                    'name': row['name'],
                    'salary':row['cost'],
                    'avgpoints':row['avg'],
                    'projpoints':row['proj']
                })
                flex['FLEX'].append({
                    'name': row['name'],
                    'salary':row['cost'],
                    'avgpoints':row['avg'],
                    'projpoints':row['proj']
                })
            elif(row['Position'] == 'TE' ):
                te['TE'].append({
                    'name': row['name'],
                    'salary':row['cost'],
                    'avgpoints':row['avg'],
                    'projpoints':row['proj']
                })
                flex['FLEX'].append({
                    'name': row['name'],
                    'salary':row['cost'],
                    'avgpoints':row['avg'],
                    'projpoints':row['proj']
                })
            elif(row['Position'] == 'QB' ):
                qb['QB'].append({
                    'name': row['name'],
                    'salary':row['cost'],
                    'avgpoints':row['avg'],
                    'projpoints':row['proj']
                })
            elif(row['Position'] == 'DST'):
                dst['DST'].append({
                    'name': row['name'],
                    'salary':row['cost'],
                    'avgpoints':row['avg'],
                    'projpoints':row['proj']
                })
    with open('DKDataConvertedToJSON/rb.txt', 'w') as outfile:  
        json.dump(rb, outfile)
    with open('DKDataConvertedToJSON/wr.txt', 'w') as outfile:  
        json.dump(wr, outfile)
    with open('DKDataConvertedToJSON/te.txt', 'w') as outfile:  
        json.dump(te, outfile)
    with open('DKDataConvertedToJSON/flex.txt', 'w') as outfile:  
        json.dump(flex, outfile)
    with open('DKDataConvertedToJSON/qb.txt', 'w') as outfile:  
        json.dump(qb, outfile)
    with open('DKDataConvertedToJSON/dst.txt', 'w') as outfile:  
        json.dump(dst, outfile)

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
                                if(salary - currentSal > 10000 and wrdata['WR'][c] != wrdata['WR'][d] and currentSal <= salary and done == False):
                                    for e in range(len(wrdata['WR'])-2):
                                        e = e + 2
                                        if(count == 500000):
                                            break
                                        currentSal = int(qb['salary']) + int(rbdata['RB'][a]['salary']) + int(rbdata['RB'][b]['salary']) + int(wrdata['WR'][c]['salary']) + int(wrdata['WR'][d]['salary']) + int(wrdata['WR'][e]['salary'])
                                        if(salary - currentSal > 7000 and wrdata['WR'][c] != wrdata['WR'][e] and wrdata['WR'][d] != wrdata['WR'][e] and currentSal <= salary and done == False):
                                            for te in tedata['TE']:
                                                if(count == 500000):
                                                    break
                                                currentSal = int(qb['salary']) + int(rbdata['RB'][a]['salary']) + int(rbdata['RB'][b]['salary']) + int(wrdata['WR'][c]['salary']) + int(wrdata['WR'][d]['salary']) + int(wrdata['WR'][e]['salary']) + int(te['salary'])
                                                if(salary - currentSal > 4500 and currentSal <= salary and done == False):
                                                    for flex in flexdata['FLEX']:
                                                        if(count == 500000):
                                                            break
                                                        currentSal = int(qb['salary']) + int(rbdata['RB'][a]['salary']) + int(rbdata['RB'][b]['salary']) + int(wrdata['WR'][c]['salary']) + int(wrdata['WR'][d]['salary']) + int(wrdata['WR'][e]['salary']) + int(te['salary']) + int(flex['salary'])
                                                        if(salary - currentSal > 2000 and flex != rbdata['RB'][a] and flex != rbdata['RB'][b] and flex != wrdata['WR'][c] and flex != wrdata['WR'][d] and flex != wrdata['WR'][e] and flex != te and currentSal <= salary and done == False):
                                                            for dst in dstdata['DST']:
                                                                if(count == 500000):
                                                                    break
                                                                currentSal = int(qb['salary']) + int(rbdata['RB'][a]['salary']) + int(rbdata['RB'][b]['salary']) + int(wrdata['WR'][c]['salary']) + int(wrdata['WR'][d]['salary']) + int(wrdata['WR'][e]['salary']) + int(te['salary']) + int(flex['salary']) + int(dst['salary'])
                                                                score = float(qb['points']) + float(rbdata['RB'][a]['points']) + float(rbdata['RB'][b]['points']) + float(wrdata['WR'][c]['points']) + float(wrdata['WR'][d]['points']) + float(wrdata['WR'][e]['points']) + float(te['points']) + float(flex['points']) + float(dst['points'])
                                                                if(currentSal <= salary and score > 175 and done == False):
                                                                    count=count+1
                                                                    print("found: " + str(count) + " QB: " + qb['name'])
                                                                    results.writerow([currentSal,score ,qb['name'] , rbdata['RB'][a]['name'], rbdata['RB'][b]['name'], wrdata['WR'][c]['name'],wrdata['WR'][d]['name'], wrdata['WR'][e]['name'], te['name'],flex['name'], dst['name']])
                                                                    if(count == 500000):
                                                                        break
                                                                    
            
    print("done.")
    
def main():
    #loadData()
    computeData()
    # rb,wr,qb,te,dst,flex = ({} for i in range(6)) 
    # rb['RB'],wr['WR'],qb['QB'],te['TE'],dst['DST'],flex['FLEX']  = ([] for i in range(6))
    
    # with open('/Users/hirro001/Desktop/pythonStuff/dk/RawDraftKingData/Book2.csv') as csvfile:
    #     reader = csv.DictReader(csvfile)
    #     for row in reader:
    #         if(row['position'] == 'DST'):
    #             dst['DST'].append({
    #                 'name': row['name'],
    #                 'salary':row['cost'],
    #                 'avgpoints':row['avg'],
    #                 'projpoints':row['proj']
    #             })

    # with open('DKDataConvertedToJSON/dst.txt', 'w') as outfile:  
    #     json.dump(dst, outfile)            



if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main()