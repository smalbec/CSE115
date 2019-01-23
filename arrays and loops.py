#x.append(x) add an item to the end of the list x

#x.pop([i]) remove the item at the given position at the list and returns it, if nothing is specifiec, a.pop() will delete the last one in the list

#len(x) returns the number of elements in the list x

def add_value(x):
    x.append(21)

def get_value(x):
    return x[7]

def sum_values(x):
    sum = x[11] + x[2] + x[12]
    return sum

def get_length(x):
    return len(x)

def create_data_structure():
    x = [13,1,-4]
    return x

def print_list(x):
    for i in range(len(x)):
        print(x[i])

def printSequence(seq):
    for x in seq:
        print(x)

def list_concat(x):
    list = " "
    for i in range(len(x)):
        list = list + x[i]
    return list


def find_value(x):
    for i in range(len(x)):
        if x[i] == 8:
            return True
    return False


def count_values(x):
    value = 0
    for i in range(len(x)):
        if x[i] > 475:
            value += 1
    return value

def count_in_range(x):
    count = 0
    for i in range(len(x)):
        if x[i]>27.18 and x[i]<43.74:
            count += 1
    return count


def sum_values(seq):
    sum = 0
    for i in seq: # goes through each number
        sum = sum + i
    return sum


import urllib.request, json


def get_ticket_data(url):
    with urllib.request.urlopen(url) as json_url:
        list = json.loads(json_url.read().decode())   #Make the url readable in a list
        value_array = []  # the new array that is gonna contain the values
        array = [] # array that is gonna contain the array with values
        for i in list:  # go trough the array
            if 'latitude' in i.keys() and 'longitude' in i.keys() and 'viodesc' in i.keys():
                lat = i['latitude']
                lon = i['longitude']
                desc = i['viodesc']
                value_array.extend([float(lat),float(lon),desc]) # push all values into an array
                array.append(value_array)  # push that array into the retun array
            value_array =  []
        return_array = json.dumps(array) #make it into a json string
    return return_array

print(get_ticket_data("https://data.buffalony.gov/resource/ux3f-ypyc.json"))