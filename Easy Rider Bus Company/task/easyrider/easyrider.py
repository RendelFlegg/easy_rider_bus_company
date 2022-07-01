import json
import re
from datetime import datetime


def check_bus_id(bus_id):
    return isinstance(bus_id, int)


def check_stop_id(stop_id):
    return isinstance(stop_id, int)


def check_stop_name(stop_name):
    try:
        *name, suffix = stop_name.rsplit()
        return name[0][0].isupper() and suffix in ('Road', 'Avenue', 'Boulevard', 'Street')
    except (AttributeError, IndexError, ValueError):
        return False


def check_next_stop(next_stop):
    return isinstance(next_stop, int)


def check_stop_type(stop_type):
    return isinstance(stop_type, str) and stop_type in ('S', 'O', 'F', '')


def check_a_time(a_time):
    pattern = r'^(([01]\d)|(2[0-3])):([0-5]\d)$'
    return isinstance(a_time, str) and bool(re.match(pattern, a_time))


def check_a_time_alt(a_time):
    try:
        datetime.strptime(a_time, '%H:%M')
        return True
    except (ValueError, TypeError):
        return False


def check_data(data):
    json_data = json.loads(data)
    error_counter = 0
    for item in json_data:
        for key in item:
            if not error_dict[key]['method'](item[key]):
                error_counter += 1
                error_dict[key]['counter'] += 1
    print(f'Type and required field validation: {error_counter} error{"" if error_counter == 1 else "s"}')
    for key in error_dict:
        if key in ('stop_name', 'stop_type', 'a_time'):
            print(f'{key}: {error_dict[key]["counter"]}')


def get_stops(data):
    stops_dict = {}
    json_data = json.loads(data)
    for item in json_data:
        bus_id = item['bus_id']
        stops_dict.setdefault(bus_id, 0)
        stops_dict[bus_id] += 1
    return stops_dict


error_dict = {'bus_id': {'method': check_bus_id, 'counter': 0},
              'stop_id': {'method': check_stop_id, 'counter': 0},
              'stop_name': {'method': check_stop_name, 'counter': 0},
              'next_stop': {'method': check_next_stop, 'counter': 0},
              'stop_type': {'method': check_stop_type, 'counter': 0},
              'a_time': {'method': check_a_time, 'counter': 0}}

stops = get_stops(input())
print('Line names and number of stops:')
for line in stops:
    print(f'bus_id: {line}, stops: {stops[line]}')
