import tensorflow_decision_forests as tfdf
import pandas as pd

data = pd.read_csv("times.csv")
data.drop(['guide'],axis=1)
print(data)

tf_train_dataset = tfdf.keras.pd_dataframe_to_tf_dataset(data, label="num_minutes")

model = tfdf.keras.RandomForestModel(verbose=0)
model.fit(tf_train_dataset)

