import json


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