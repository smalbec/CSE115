def count_chars(filename):
    with open(filename) as f:
        count = 0
        for line in f:
            line = line.rstrip('\r\n')
            count = count + len(line)
    return count;


def count_spaces(filename):
    with open(filename) as f:
        count = 0



def countCharacter(filename):
    count = {}
    with open(filename) as f:
        for line in f:
            for ch in line:
                if ch in count:
                    count[ch] = count[ch] + 1
                else:
                    count[ch] = 1
    return


import re

def countWords(filename):
    count = {}
    with open(filename) as f:
        for line in f:
            wordList = re.split("[^a-zA-Z']+", line)   #why the quotes have to be the double ones to work?
            for word in wordList:
                if word in count:
                    count[word] = count[word] + 1
                else:
                    count[word] = 1

    return count



def overspent(budget):
    over = {}
    months = list(budget.keys())
    months.pop(0)
    for key in months:
        data = budget[key] #This is how you access an array inside the value of the dictionary
        diff = int(data[0]) - int(data[1])
        if (diff < 0):
            over[key] = diff
    return over

#CSV READING

#When calling a certain line/row, remember arrays start at 0, so line 2 is line[1]


import csv #REMEMBER THIS

def readBudget(filename):
    budget = {}
    with open(filename, newline='') as f: #remember this
        reader = csv.reader(f) #remember this
        for line in reader:
            month = line[0]
            line.pop(0)
            budget[month] = line
    return budget


#Lab prep

def count_lines(filename):
    with open(filename) as f:
        count = 0
        for line in f:
            count = count + 1
    return count

def file_to_int_list():
    list = []
    with open("creativity.txt") as f:
        for line in f:
            list.append(int(line))
    return list

def sum_ints():
    sum = 0
    with open('specialty.txt') as f:
        for line in f:
            sum = int(line) + sum
    return sum


def file_to_list():
    list = []
    with open('grain.txt') as f:
        for line in f:
            line = line.rstrip('\r\n')
            list.append(line)
    return list


def average_ints():
    sum = 0
    average = 0
    count = 0
    with open('accurately.txt') as f:
        for line in f:
            sum += int(line)
            count += 1
    average = sum / count
    return average


import csv

def csv_sum(filename):
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        sum = 0
        count = 0
        for line in reader:
            sum = sum + float(line[0])
    return sum


import csv

def csv_average(filename):
    sum = 0
    count = 0
    with open(filename,newline = '') as f:
        reader = csv.reader(f)
        for line in reader:
            sum = sum + int(line[3])
            count += 1
        average = sum / count
    return average

import csv

def csv_to_kvs(filename):
    budget = {}
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        for line in reader:
            month = line[0]
            budget[month] = float(line[1])
    return budget


import csv


def csv_to_list(filename):
    x = []
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        for line in reader:
            x.append(int(line[4]))
    return x

import csv

def average_rating(filename, songid):
    sum = 0
    count = 0
    with open(filename,newline = '') as f:
        reader = csv.reader(f)
        for line in reader:
            if line[0] == songid:
                sum = sum + int(line[3])
                count += 1
    average = sum / count
    return average



import csv

def total_population(filename,list):
    totalpopulation = 0
    with open(filename,newline = '') as f:
        reader = csv.reader(f)
        for line in reader:
            for i in range(len(list)):  #You changed from list to range(len(list)) and it worked, WHY
                if line[0] == list[i][0] and line[1] == list[i][1] and line[2] == list[i][2]:
                    totalpopulation += int(line[3])
    return totalpopulation


import csv


def quantities_owned(tradesfile):
    quantity_stock = {}
    with open(tradesfile,newline='') as f:
        reader = csv.reader(f)

        for line in reader:
            ticker = line[2]
            stock_amount = int(line[1])

            if ticker in quantity_stock:
                if line[0] == 'buy':
                    quantity_stock[ticker] += stock_amount
                else:
                    quantity_stock[ticker] -= stock_amount
            else:
                quantity_stock[ticker] = stock_amount

    return quantity_stock



import csv


def read_prices(list_tickers):
    tickers_dict = {}
    for i in list_tickers:
        tickers_dict[i] = date_prices(i)
    return tickers_dict


def date_prices(list_tickers):
    date_prices_dict = {}
    filename = list_tickers + ".csv"
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        for line in reader:
            date_prices_dict[line[0]] = float(line[1])
    return date_prices_dict


import csv

def portfolio_value(tradesfile):
    totalvalue = 0
    checklit = []

    with open(tradesfile, newline='') as f:
        reader = csv.reader(f)
        for line in reader:
            if line[2] not in checklit:
                checklit.append(line[2])
                for i in date_prices(line[2]):
                    if i == "2015-12-31":
                        totalvalue += date_prices(line[2])[i] * quantities_owned(tradesfile)[line[2]]

        return totalvalue


def quantities_owned(tradesfile):
    quantity_stock = {}
    with open(tradesfile, newline='') as m:
        reader = csv.reader(m)
        for line in reader:
            ticker = line[2]
            stock_amount = int(line[1])
            if ticker in quantity_stock:
                if line[0] == 'buy':
                    quantity_stock[ticker] += stock_amount
                else:
                    quantity_stock[ticker] -= stock_amount
            else:
                quantity_stock[ticker] = stock_amount

    return quantity_stock

def read_prices(list_tickers):
    tickers_dict = {}
    for i in list_tickers:
        tickers_dict[i] = date_prices(i)
    return tickers_dict

def date_prices(list_tickers):
    date_prices_dict = {}
    filename = list_tickers + ".csv"
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        for line in reader:
            date_prices_dict[line[0]] = float(line[1])
    return date_prices_dict


