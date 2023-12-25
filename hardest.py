from utils.model import *
from utils.data import *

model = load_model()
_, not_done = load_boxes()

orded_boxes = []
for picked in not_done:
    x = create_prediction_data(picked)
    predictions = model.predict(x,verbose=0)
    min_pred = round(predictions[0][0])
    orded_boxes.append([picked,min_pred])

orded_boxes = sorted(orded_boxes, key=lambda x: x[1])
picked = orded_boxes[-1]
picked = picked[0]
picked,now = load_start(picked)
print("Do: ",picked['name'])
guide = input("Did you use  a guide [1/0]?")
write_done([picked['name']])
write_times(now,guide,picked)