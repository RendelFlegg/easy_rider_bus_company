import json
import re
from datetime import datetime


def check_bus_id(bus_id):
    return isinstance(bus_id, int)


def check_stop_id(stop_id):
    return isinstance(stop_id, int)


def check_stop_name(stop_name):
    return isinstance(stop_name, str) and stop_name != ''


def check_stop_name_alt(stop_name):
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
    pattern = r'([01]\d|2[0-3]):([0-5]\d)'
    return isinstance(a_time, str) and bool(re.match(pattern, a_time))


def check_a_time_alt(a_time):
    try:
        datetime.strptime(a_time, '%H:%M')
        return True
    except (ValueError, TypeError):
        return False


json_data = '[{"bus_id": 128, "stop_id": 1, "stop_name": "Prospekt Avenue", "next_stop": 3, "stop_type": "S", "a_time": 8.12}, ' \
             '{"bus_id": 128, "stop_id": 3, "stop_name": "", "next_stop": 5, "stop_type": "", "a_time": "08:19"}, ' \
             '{"bus_id": 128, "stop_id": 5, "stop_name": "Fifth Avenue", "next_stop": 7, "stop_type": "O", "a_time": "08:25"}, ' \
             '{"bus_id": 128, "stop_id": "7", "stop_name": "Sesame Street", "next_stop": 0, "stop_type": "F", "a_time": "08:37"}, ' \
             '{"bus_id": "", "stop_id": 2, "stop_name": "Pilotow Street", "next_stop": 3, "stop_type": "S", "a_time": ""}, ' \
             '{"bus_id": 256, "stop_id": 3, "stop_name": "Elm Street", "next_stop": 6, "stop_type": "", "a_time": "09:45"}, ' \
             '{"bus_id": 256, "stop_id": 6, "stop_name": "Sunset Boulevard", "next_stop": 7, "stop_type": "", "a_time": "09:59"}, ' \
             '{"bus_id": 256, "stop_id": 7, "stop_name": "Sesame Street", "next_stop": "0", "stop_type": "F", "a_time": "10:12"}, ' \
             '{"bus_id": 512, "stop_id": 4, "stop_name": "Bourbon Street", "next_stop": 6, "stop_type": "S", "a_time": "08:13"}, ' \
             '{"bus_id": "512", "stop_id": 6, "stop_name": "Sunset Boulevard", "next_stop": 0, "stop_type": 5, "a_time": "08:16"}]'


error_counter = 0
error_dict = {'bus_id': {'method': check_bus_id, 'counter': 0},
              'stop_id': {'method': check_stop_id, 'counter': 0},
              'stop_name': {'method': check_stop_name, 'counter': 0},
              'next_stop': {'method': check_next_stop, 'counter': 0},
              'stop_type': {'method': check_stop_type, 'counter': 0},
              'a_time': {'method': check_a_time, 'counter': 0}}

json_data = input()

test_json = json.loads(json_data)
for item in test_json:
    for key in item:
        if not error_dict[key]['method'](item[key]):
            error_counter += 1
            error_dict[key]['counter'] += 1

print(f'Type and required field validation: {error_counter} error{"" if error_counter == 1 else "s"}')
for key in error_dict:
    print(f'{key}: {error_dict[key]["counter"]}')