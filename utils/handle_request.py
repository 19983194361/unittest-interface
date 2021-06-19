import requests
from utils.handle_config import get_config

base_url = get_config('environment')


def send(case):
    method = case['method'].upper()
    url = base_url['base_url'] + case['path']
    headers = eval(case['headers'])
    if method == 'GET':
        param = eval(case['param'])
        return requests.get(url=url, param=param, headers=headers).json()
    elif method == 'POST':
        if headers['Content-Type'] == 'application/x-www-form-urlencoded':
            data = case['data']
            return requests.post(url=url, data=data, headers=headers).json()
        if headers['Content-Type'] == 'application/json':
            json = eval(case['json'])
            return requests.post(url=url, json=json, headers=headers).json()
    elif method == 'PUT':
        if headers['Content-Type'] == 'application/x-www-form-urlencoded':
            data = case['data']
            return requests.put(url=url, data=data, headers=headers).json()
        if headers['Content-Type'] == 'application/json':
            json = eval(case['json'])
            return requests.put(url=url, json=json, headers=headers).json()
    elif method == 'DELETE':
        return requests.delete(url=url, headers=headers).json()
