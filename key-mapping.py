# Called a dictionary in python
# Pair of braces creates an empty dictionary
#You can add initial key:value to the dictionary


a = {}

x = {'a' : 1, 'b' : 2,  'c' : 3}

#Add with x['key'] = value

x ['c'] = 12

x = {'a' : 1, 'b' : 2, 'c' : 12}


#Update and add with x.update(y)

x.update({'b': 7, 'z' : 3})

x = {'a' : 1, 'b' : 7, 'c' : 12, 'z' : 3}


#x.get(key)

x.get('c')
12


x.get('q', False)
False

#del x[key]


#Sequences: x.keys() returns each of the keys of the dictionary
#x.values() returns each of the values
#x.itmes() both

#Lists: list(x) turns the sequence into a list

#test

def get_stat(x):
    return x['Constitution']

def add_key_value(x):
    x['its'] = 10


def get_value(x):
    if 'pratical' in x:
        return x['pratical']
    else:
        return 0

def print_keys(x):
    for i in x.keys():
        print(i)

def indexed_kvs():
    x = {}
    for i in range(39):
       x.update({str(i): i})
    return x

def get_size(x):
    sum = 0
    for i in list(x.items()):
        sum += 1
    return sum

#OR MUCH SIMPLER APPROACH, DUMMY

def get_size(x):
    return len(x)

def find_value(x):
    for i in x.values():
        if i == 6:
            return True
    return False

#or much simpler approach, small brain

def find_value(x):
    if 6 in x.values():
        return True
    return False

def find_key(x):
    for i in x.keys():
        if i == 'dig':
            return True
    return False

def valueCount(dict,val):
    answer = 0
    for v in dict.values():
        if v==val:
            answer = answer + 1
    return answer


def matchedKeys(dict, val):
    answer = []
    for it in dict.items():
        k,v = it
        if v==val:
            answer.append(k)
    return answer



