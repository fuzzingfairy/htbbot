import random
import json
import csv
import tqdm
import vowpalwabbit
import time
import datetime

import csv
train_min_examples = []
train_guide_examples = []

with open('times.csv', newline='') as csvfile:
    spamreader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        data = str(row['num_minutes'])
        dataguide = str(row['guide'])
        data += " | "
        dataguide += " | "
        for key in row:
            if not key in ['num_minutes','guide']:
                data += key+":"+row[key] + " "
                dataguide += key+":"+row[key] + " "
        
        train_min_examples.append(data)
        train_guide_examples.append(dataguide)

csvfile.close()


print("training models :)")
for example in  tqdm.tqdm(train_min_examples):
    model.learn(example)

for example in tqdm.tqdm(train_guide_examples):
    model1.learn(example)

with open("data.json","r") as f:
    data = json.load(f)
print()
print()

real = data

count = 0
total = len(data)

not_done =  []
for i in real:
    if i['authUserInRootOwns']:
       # print(count)
        count += 1
    else:
        not_done.append(i)



tqdm.tqdm(initial=count,total=len(real),desc="Percentage HTB Owned",unit="boxes",unit_scale=False)

picked = random.choice(not_done)

features = [
    picked['static_points'],
    picked['star'],
    picked['difficulty'],
    picked['os'],
    picked['difficultyText'],
    picked['user_owns_count'],
    picked['root_owns_count'],
    picked['feedbackForChart']['counterCake'],
    picked['feedbackForChart']['counterTooEasy'],
    picked['feedbackForChart']['counterMedium'],
    picked['feedbackForChart']['counterBitHard'],
    picked['feedbackForChart']['counterTooHard'],
    picked['feedbackForChart']['counterExHard'],
    picked['feedbackForChart']['counterBrainFuck'],
    picked['recommended']


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
]

test_example = "| "
for idx, i in enumerate(fieldnames[4:]):
        test_example += fieldnames[idx+4] + ":"+str(features[idx]) + " "


min_pred = model.predict(test_example)
guide_pred = model1.predict(test_example)


print("Do: " + picked['name'] + " " + str(round(min_pred)) + "min " + str(guide_pred))
start = datetime.datetime.now()
withguide =  input("Did you look at a guide [0/1]: ")
finish = datetime.datetime.now()

elapsed = finish-start

num_minutes = round(elapsed.seconds/60)
print("Done in " + str(num_minutes))

import csv
now = datetime.datetime.now()
mins = now.hour*60 + now.minute
with open(r'times.csv', 'a', newline='') as csvfile:

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    rowdict = {'num_minutes':num_minutes,'guide':withguide}
    for idx, i in enumerate(fieldnames[4:]):
        rowdict[fieldnames[idx+4]]=  features[idx]

    rowdict["tod"] = mins
    rowdict["dayofweek"] =  now.weekday()


    writer.writerow(rowdict)



for idx,i in enumerate(results):
    if i['name'] == picked['name']:
        results[idx]['authUserInRootOwns'] = True

with open('data.json','w') as f:
    json.dump(results, f)