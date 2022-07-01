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
    json_data = json.loads(data)
    lines_dict = {}
    for item in json_data:
        bus_id = item['bus_id']
        lines_dict.setdefault(bus_id, 0)
        lines_dict[bus_id] += 1
    print('Line names and number of stops:')
    for line in lines_dict:
        print(f'bus_id: {line}, stops: {lines_dict[line]}')
    return lines_dict


def get_route_dictionary(data):
    json_data = json.loads(data)
    route_dict = {}
    for item in json_data:
        bus_id = item['bus_id']
        stop_name = item['stop_name']
        stop_type = item['stop_type']
        route_dict.setdefault(bus_id, {'start': '', 'finish': '', 'stops': set()})
        route_dict[bus_id]['stops'].add(stop_name)
        if stop_type == 'S':
            if route_dict[bus_id]['start'] != '':
                return bus_id
            else:
                route_dict[bus_id]['start'] = stop_name
        if stop_type == 'F':
            if route_dict[bus_id]['finish'] != '':
                return bus_id
            else:
                route_dict[bus_id]['finish'] = stop_name
    return route_dict


def process_route_dictionary(route_dict):
    start_stops = set()
    transfer_stops = set()
    finish_stops = set()
    list_of_routes = list(route_dict.keys())
    while list_of_routes:
        test_item = list_of_routes.pop()
        if route_dict[test_item]['start'] == '' or route_dict[test_item]['finish'] == '':
            print(f'There is no start or end stop for the line: {test_item}.')
            return False
        start_stops.add(route_dict[test_item]['start'])
        finish_stops.add(route_dict[test_item]['finish'])
        for route in list_of_routes:
            transfer_stops.update(route_dict[test_item]['stops'].intersection(route_dict[route]['stops']))
    start_stops = sorted(list(start_stops))
    transfer_stops = sorted(list(transfer_stops))
    finish_stops = sorted(list(finish_stops))
    print('Start stops:', len(start_stops), start_stops)
    print('Transfer stops:', len(transfer_stops), transfer_stops)
    print('Finish stops:', len(finish_stops), finish_stops)


def arrival_time_test(data):
    json_data = json.loads(data)
    bus_dict = {}
    err_dict = {}
    for item in json_data:
        bus_id = item['bus_id']
        a_time = datetime.strptime(item['a_time'], '%H:%M')
        bus_dict.setdefault(bus_id, datetime(1899, 1, 1))
        if a_time > bus_dict[bus_id]:
            bus_dict[bus_id] = a_time
        elif bus_id not in err_dict:
            err_dict[bus_id] = item['stop_name']
    print('Arrival time test:')
    if err_dict:
        for error in err_dict:
            print(f'bus_id line {error}: wrong time on station {err_dict[error]}')
    else:
        print('OK')


error_dict = {'bus_id': {'method': check_bus_id, 'counter': 0},
              'stop_id': {'method': check_stop_id, 'counter': 0},
              'stop_name': {'method': check_stop_name, 'counter': 0},
              'next_stop': {'method': check_next_stop, 'counter': 0},
              'stop_type': {'method': check_stop_type, 'counter': 0},
              'a_time': {'method': check_a_time, 'counter': 0}}

arrival_time_test(input())
