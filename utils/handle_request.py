import requests
from utils.handle_config import get_config
from utils.handle_log import logger

base_url = get_config('environment')


def send(case):
    name = case['name']
    logger.info('[{}]正在处理数据，请稍等...'.format(name))
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
            logger.info('[{}]数据处理完毕！'.format(name))
            logger.info('[{}]正在发送请求，请稍等...'.format(name))
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
