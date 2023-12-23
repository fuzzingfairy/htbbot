import random
import json
import csv
import tqdm
import time
import datetime
import pandas as pd
import seaborn as sns
import tensorflow as tf
import numpy as np
import tensorflow.keras.layers as layers
import tensorflow.keras as keras


import matplotlib.pyplot as plt
plt.show()

data = pd.read_csv("times.csv")
dataset = data.drop(['guide'],axis=1)

train_dataset = dataset.sample(frac=1, random_state=0)
test_dataset = dataset.drop(train_dataset.index)
test_dataset = np.asarray(test_dataset).astype(np.float32)
lookup = layers.StringLookup(output_mode="one_hot")
print(train_dataset.to_string())

def dataframe_to_dataset(dataframe):
    dataframe = dataframe.copy()
    labels = dataframe.pop("num_minutes")
    ds = tf.data.Dataset.from_tensor_slices((dict(dataframe), labels))
    ds = ds.shuffle(buffer_size=len(dataframe))
    return ds


def encode_numerical_feature(feature, name, dataset):
    # Create a Normalization layer for our feature
    normalizer = layers.Normalization()

    # Prepare a Dataset that only yields our feature
    feature_ds = dataset.map(lambda x, y: x[name])
    feature_ds = feature_ds.map(lambda x: tf.expand_dims(x, -1))

    # Learn the statistics of the data
    normalizer.adapt(feature_ds)

    # Normalize the input feature
    encoded_feature = normalizer(feature)
    return encoded_feature


def encode_categorical_feature(feature, name, dataset, is_string):
    lookup_class = layers.StringLookup if is_string else layers.IntegerLookup
    # Create a lookup layer which will turn strings into integer indices
    lookup = lookup_class(output_mode="binary")

    # Prepare a Dataset that only yields our feature
    feature_ds = dataset.map(lambda x, y: x[name])
    feature_ds = feature_ds.map(lambda x: tf.expand_dims(x, -1))

    # Learn the set of possible string values and assign them a fixed integer index
    lookup.adapt(feature_ds)

    # Turn the string input into integer indices
    encoded_feature = lookup(feature)
    return encoded_feature

train_ds = dataframe_to_dataset(train_dataset)

for x, y in train_ds.take(1):
    print("Input:", x)
    print("Target:", y)

print(train_ds)

tod = keras.Input(shape=(1,), name="tod", dtype="int64")
dayofweek = keras.Input(shape=(1,), name="dayofweek", dtype="int64")
static_points = keras.Input(shape=(1,), name="static_points", dtype="int64")
star = keras.Input(shape=(1,), name="star")
difficulty = keras.Input(shape=(1,), name="difficulty", dtype="int64")
os = keras.Input(shape=(1,), name="os", dtype="string")
difficultyText = keras.Input(shape=(1,), name="difficultyText",dtype="string")

user_owns_count = keras.Input(shape=(1,), name="root_owns_count", dtype="int64")
root_owns_count = keras.Input(shape=(1,), name="user_owns_count", dtype="int64")


all_inputs = [
    tod,
    dayofweek,
    os,
    difficultyText]



tod_encoded = encode_numerical_feature(tod, "tod", train_ds)
daysofweek_encoded = encode_numerical_feature(dayofweek,"dayofweek",train_ds)
os_encoded = encode_categorical_feature(os, "os", train_ds, True)
difficultyText_encoded = encode_categorical_feature(difficultyText, "difficultyText", train_ds, True)

all_features = layers.concatenate(
    [
        tod_encoded,
        daysofweek_encoded,
        os_encoded,
        difficultyText_encoded
    ]
)

train_ds = train_ds.batch(2)


#all_features = tf.reshape(all_features,shape=(,7))
x = layers.Dense(32, activation="relu")(all_features)
x = layers.Dropout(0.5)(x)
output = layers.Dense(1, activation="sigmoid")(x)
model = keras.Model(all_inputs, output)
model.compile("adam", "binary_crossentropy", metrics=["mae"])
keras.utils.plot_model(model, show_shapes=True, rankdir="LR")

model.summary()
model.fit(train_ds, epochs=1)


print("DONE")

print(train_dataset.to_string())

sns.pairplot(train_dataset[['num_minutes', 'difficulty', 'user_owns_count']], diag_kind='kde')
plt.show()

print(train_dataset.describe().transpose())

train_features = train_dataset.copy()
test_features = test_dataset.copy()

train_labels = train_features.pop('num_minutes')
test_labels = test_features.pop('num_minutes')


normalizer = tf.keras.layers.Normalization(axis=-1)
normalizer.adapt(np.array(train_features))





def build_and_compile_model(norm):
  model = keras.Sequential([
      norm,
      layers.Dense(64, activation='relu'),
      layers.Dense(64, activation='relu'),
      layers.Dense(1)
  ])

  model.compile(loss='mean_absolute_error',
                optimizer=tf.keras.optimizers.Adam(0.001))
  return model

dnn_horsepower_model = build_and_compile_model(normalizer)
dnn_model.summary()

history = dnn_horsepower_model.fit(
    train_features,
    train_labels,
    validation_split=0.2,
    verbose=0, epochs=100)


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
