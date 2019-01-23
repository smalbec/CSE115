import urllib.request

def get_response(str1,str2,str3):
    url = str1 + "://" + str2 + "/" + str3
    response = urllib.request.urlopen(url)
    content = response.read().decode()
    return content


    def get_response():
        url = 'https://fury.cse.buffalo.edu/ps-api/r/various'
        response = urllib.request.urlopen(url)
        content = response.read().decode()
        return content

import urllib.request,json

def query_string():
    url = 'https://fury.cse.buffalo.edu/ps-api/a?' + "x=1&y=1&z=3"
    response = urllib.request.urlopen(url)
    content = response.read().decode()
    obj = json.loads(content)
    value = obj['answer']
    return value

import urllib.request,json

def query_dict(dict)    :
    url = 'https://fury.cse.buffalo.edu/ps-api/a?'
    query = ''
    for i in dict:
        query = query + i + '=' + str(dict[i]) + '&'
    query_url = url + query
    response = urllib.request.urlopen(query_url)
    content = response.read().decode()
    obj = json.loads(content)
    value = obj['answer']
    return value

import urllib.request,json

def flu_season():
    url = 'https://fury.cse.buffalo.edu/ps-api/flutrack/?' + 'time=3'
    response = urllib.request.urlopen(url)
    content = response.read().decode()
    obj = json.loads(content)
    count = 0
    for i in obj:
        count += 1
    return count