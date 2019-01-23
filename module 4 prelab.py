import math, sqlite3


def sort_distance(arr):
    return int(arr[6])


def closest_cities():
    arr = []
    lat_arr = []
    lon_arr = []
    cities_arr = get_us_cities()
    cities_arr_distance = get_us_cities()

    for i in cities_arr:
        lat_arr.append(i[4])
        lon_arr.append(i[5])

    for i in cities_arr_distance:
        i.append(great_circle_distance(43.0023092, -78.7876885, i[4], i[5]))

    cities_arr_distance.sort(key=sort_distance)

    for i in cities_arr_distance:
        i.pop(6)

    return cities_arr_distance


def great_circle_distance(lat1, lon1, lat2, lon2):
    R = 6371
    φ1 = math.radians(lat1)
    φ2 = math.radians(lat2)
    Δφ = math.radians(lat2 - lat1)
    Δλ = math.radians(lon2 - lon1)

    a = math.sin(Δφ / 2) * math.sin(Δφ / 2) + math.cos(φ1) * math.cos(φ2) * math.sin(Δλ / 2) * math.sin(Δλ / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    d = R * c

    return d


conn = sqlite3.connect('city_data.db')
cur = conn.cursor()


def get_us_cities():
    arr = []
    small_arr = []
    cur.execute('SELECT * FROM cities')
    for i in cur:
        if i[0] == 'us':
            small_arr.extend([i[0], i[1], i[2], i[3], i[4], i[5]])
            arr.append(small_arr)
            small_arr = []
    return arr