# sorting


def sort_list(arr):
    arr.sort()
    return


# sorting in an array of objects for specific key

def strikekey(arr):
    return arr['strike']


def sort_kvs(arr):
    arr.sort(key=strikekey)


# sorting in an array of array for the 2nd value
def indexkey(arr):
    return arr[1]


def sort_by_index(arr):
    arr.sort(key=indexkey)
    return


# sorting by len

def sortlen(arr):
    return len(arr)


def sort_by_length(arr):
    arr.sort(key=sortlen)


# sort between the products
def productkey(arr):
    return arr[1] * arr[4]


def sort_by_product(arr):
    arr.sort(key=productkey)


# sort through average of a list in an object inan array

def averagekey(arr):
    count = 0
    sum = 0
    for i in arr['ratings']:
        count += 1
        sum += i
    average = sum / count
    return average


def sort_by_average_rating(arr):
    arr.sort(key=averagekey)
