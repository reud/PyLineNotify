# coding:UTF-8
import os
import requests


def output(strings: str):
    """
    引数に与えられた文字列をLINENotifyで通知する関数
    :param strings:
        通知する文字列
    :return None:
    """
    print(strings)
    url = 'https://notify-api.line.me/api/notify'
    token = str(os.getenv('NOTIFER_TOKEN'))
    headders = {'Authorization': 'Bearer ' + token}
    message = strings
    payload = {'message': message}
    res = requests.post(url, data=payload, headers=headders)
    print(f'LINENotify:{res}')