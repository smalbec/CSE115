import json


def read_json(jsonstr):
    content = json.loads(jsonstr)
    return content

def to_json(string):
    oontent = json.dumps(string)
    return content




def get_value(json_str):
    obj = json.loads(json_str)
    value = obj['release']
    return value

def get_y(json_object):
    obj = json.loads(json_object)
    count = 0
    while obj['x'][count] != -7:
        count += 1
    return obj['y'][count]

def json_average(json_str):
    arr = json.loads(json_str)
    average = 0
    sum = 0
    count = 0
    for i in arr:
        sum += i['temperature']
        count += 1
    average = sum / count
    average_obj = {'temperature':average}
    json_str = json.dumps(average_obj)
    return json_str

def json_filter(json_str):
    arr = json.loads(json_str)
    new_arr = []
    for i in arr:
        if i['velocity'] >44.3:
            new_arr.append(i)
    json_str = json.dumps(new_arr)
    return json_str