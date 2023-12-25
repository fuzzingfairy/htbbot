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

# https://keras.io/examples/structured_data/structured_data_classification_from_scratch/

import matplotlib.pyplot as plt

data = pd.read_csv("times.csv")


dataframe = data.drop(['guide'],axis=1)

for col in dataframe.columns:
    print(col)

print(dataframe)

val_dataframe = dataframe.sample(frac=0, random_state=1337)
train_dataframe = dataframe.drop(val_dataframe.index)



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

train_ds = dataframe_to_dataset(train_dataframe)
#val_ds = dataframe_to_dataset(val_dataframe)




tod = keras.Input(shape=(1,), name="tod", dtype="int64")
dayofweek = keras.Input(shape=(1,), name="dayofweek", dtype="int64")
static_points = keras.Input(shape=(1,), name="static_points", dtype="int64")
star = keras.Input(shape=(1,), name="star")
difficulty = keras.Input(shape=(1,), name="difficulty", dtype="int64")
os = keras.Input(shape=(1,), name="os", dtype="string")
difficultyText = keras.Input(shape=(1,), name="difficultyText",dtype="string")

user_owns_count = keras.Input(shape=(1,), name="root_owns_count", dtype="int64")
root_owns_count = keras.Input(shape=(1,), name="user_owns_count", dtype="int64")

counterCake = keras.Input(shape=(1,), name='counterCake',dtype="int64")
counterTooEasy = keras.Input(shape=(1,), name='counterTooEasy',dtype="int64")
counterMedium = keras.Input(shape=(1,), name='counterMedium',dtype="int64")
counterBitHard = keras.Input(shape=(1,), name='counterBitHard',dtype="int64")
counterTooHard = keras.Input(shape=(1,), name='counterTooHard',dtype="int64")
counterExHard = keras.Input(shape=(1,), name='counterExHard',dtype="int64")
counterBrainFuck = keras.Input(shape=(1,), name='counterBrainFuck',dtype="int64")
recommended = keras.Input(shape=(1,),name='recommended',dtype="int64")




all_inputs = [
    tod,
    dayofweek,
    static_points,
    star,
    difficulty,
    os,
    difficultyText,
    user_owns_count,
    root_owns_count,
    counterCake,
    counterTooEasy,
    counterMedium,
    counterBitHard,
    counterTooHard,
    counterExHard,
    counterBrainFuck,
    recommended, 
    ]



tod_encoded = encode_numerical_feature(tod, "tod", train_ds)
daysofweek_encoded = encode_numerical_feature(dayofweek,"dayofweek",train_ds)
static_points_encoded =  encode_numerical_feature(static_points,"static_points",train_ds)
star_encoded = encode_numerical_feature(star,"star",train_ds)
difficulty_encoded = encode_numerical_feature(difficulty,"difficulty",train_ds)
os_encoded = encode_categorical_feature(os, "os", train_ds, True)
difficultyText_encoded = encode_categorical_feature(difficultyText, "difficultyText", train_ds, True)
user_owns_count_encoded = encode_numerical_feature(user_owns_count,"user_owns_count",train_ds)
root_owns_count_encoded = encode_numerical_feature(root_owns_count,"root_owns_count",train_ds)


counterCake_encoded = encode_numerical_feature(counterCake,"counterCake",train_ds)
counterTooEasy_encoded = encode_numerical_feature(counterTooEasy,"counterTooEasy",train_ds)
counterMedium_encoded = encode_numerical_feature(counterMedium,"counterMedium",train_ds)
counterBitHard_encoded = encode_numerical_feature(counterBitHard,"counterBitHard",train_ds)
counterTooHard_encoded = encode_numerical_feature(counterTooHard,"counterTooHard",train_ds)
counterExHard_encoded = encode_numerical_feature(counterExHard,"counterExHard",train_ds)
counterBrainFuck_encoded = encode_numerical_feature(counterBrainFuck,"counterBrainFuck",train_ds)

recommended_encoded = encode_numerical_feature(recommended,"recommended",train_ds)






all_features = layers.concatenate(
    [
    tod_encoded,
    daysofweek_encoded,
    static_points_encoded,
    star_encoded,
    difficulty_encoded,
    os_encoded,
    difficultyText_encoded,
    user_owns_count_encoded,
    root_owns_count_encoded,
    counterCake_encoded,
    counterTooEasy_encoded,
    counterMedium_encoded,
    counterBitHard_encoded,
    counterTooHard_encoded,
    counterExHard_encoded,
    counterBrainFuck_encoded,
    recommended_encoded, 
    ]
)

train_ds = train_ds.batch(1)
#sval_ds = val_ds.batch(1)


things = []

x = layers.Dense(32, activation="relu")(all_features)
x = layers.Dropout(0.5)(x)
output = layers.Dense(1, activation="relu")(x)
model = keras.Model(all_inputs, output)
model.compile("adam", "binary_crossentropy", metrics=["mse"])
log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=0)


model.summary()
#model.fit(train_ds, epochs=50,validation_data=val_ds, callbacks=[tensorboard_callback])


history = model.fit(train_ds, epochs=60,callbacks=[tensorboard_callback])

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

res = []
for picked in not_done:
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


    preds = {}
    for idx, i in enumerate(fieldnames[4:]):
        preds[fieldnames[idx+4]] = features[idx]

    #print(preds)


    now = datetime.datetime.now()
    mins = now.hour*60 + now.minute
    preds['tod'] = mins
    preds['dayofweek'] = now.weekday()
    input_dict = {name: tf.convert_to_tensor([value]) for name, value in preds.items()}
    predictions = model.predict(input_dict,verbose=0)
    min_pred = round(predictions[0][0])
    #print(picked['name'],min_pred)
    res.append([picked['name'],min_pred])


res = sorted(res, key=lambda x: x[1])

for i in res[0:3]:
    print(i[0],i[1])
