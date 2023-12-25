import json
import os 
import pickle
import datetime
import csv

def load_boxes():
    with open("data/data.json","r") as f:
        data = json.load(f)


    count = 0
    total = len(data)



    not_done =  []
    for i in data:
        if i['authUserInRootOwns']:
        # print(count)
            count += 1
        else:
            not_done.append(i)

    return data, not_done

def write_done(boxes):
    with open('data/data.json','r') as f:
        real = json.load( f)

    for idx,i in enumerate(real):
        if i['name'] in boxes:
            real[idx]['authUserInRootOwns'] = True


    with open('data/data.json','w') as f:
        json.dump(real, f)


firstlookup = [
        'static_points',
        'star',
        'difficulty',
        'os',
        'difficultyText',
        'user_owns_count',
        'root_owns_count',
        'recommended',

]

nestedfieldnames = [
      'counterCake',
        'counterTooEasy',
        'counterMedium',
        'counterBitHard',
        'counterTooHard',
        'counterExHard',
        'counterBrainFuck'
]


fieldnames = [
        'num_minutes',
        'guide',
        'tod',
        'dayofweek',
        'static_points',
        'star',
        'difficulty',
        'os',
        'difficultyText',
        'user_owns_count',
        'root_owns_count',
        'counterCake',
        'counterTooEasy',
        'counterMedium',
        'counterBitHard',
        'counterTooHard',
        'counterExHard',
        'counterBrainFuck',
        'recommended',
        'name',
        'date'
]

def write_times(now,guide,boxinfo):
    with open(r'data/times.csv', 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        data = {}
        data['guide'] = guide
        data['name'] = boxinfo['name']

        for i in firstlookup:
            data[i] = boxinfo[i]
        
        for i in nestedfieldnames:
            data[i] = boxinfo['feedbackForChart'][i]
        

        data["tod"] = now.hour*60 + now.minute
        data["dayofweek"] =  now.weekday()
        data['date'] = datetime.datetime.now().strftime("%m-%d-%Y")
        finish = datetime.datetime.now()
        elapsed = finish-now
        data['num_minutes'] = round(elapsed.seconds/60)
        writer.writerow(data)
    os.remove("data/picked.pickle") 
    os.remove("data/now.pickle") 

def load_start(picked):
    if os.path.isfile("picked.pickle"):
        with open("data/picked.pickle","rb") as f:
            picked = pickle.load(f)

        with open('data/now.pickle',"rb") as f:
            now = pickle.load(f)
            finish = datetime.datetime.now()
            elapsed = finish-now
            num_minutes = round(elapsed.seconds/60)
            print("Been going for " + str(num_minutes))

    else:  
        now = datetime.datetime.now()

    return picked, now
