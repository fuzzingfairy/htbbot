import random
import json
import csv
import tqdm
import vowpalwabbit
import time
import datetime

import tensorflow_decision_forests as tfdf
import pandas as pd

data = pd.read_csv("times.csv")
data = data.drop(['guide'],axis=1)
print(data)

tf_train_dataset = tfdf.keras.pd_dataframe_to_tf_dataset(data, label="num_minutes",task=tfdf.keras.Task.REGRESSION)

model = tfdf.keras.RandomForestModel(verbose=0,task = tfdf.keras.Task.REGRESSION)
model.fit(tf_train_dataset)



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


preds = {}
for idx, i in enumerate(fieldnames[4:]):
    preds[fieldnames[idx+4]] = [features[idx]]

print(preds)
now = datetime.datetime.now()
mins = now.hour*60 + now.minute
preds['tod'] = mins
preds['dayofweek'] = now.weekday()

preds = pd.DataFrame(preds)
print(preds)
preds = tfdf.keras.pd_dataframe_to_tf_dataset(preds,task=tfdf.keras.Task.REGRESSION)
print(model.predict(preds))

min_pred = 2
guide_pred =1

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



for idx,i in enumerate(real):
    if i['name'] == picked['name']:
        results[idx]['authUserInRootOwns'] = True


with open('data.json','w') as f:
    json.dump(results, f)
