# coding:UTF-8
import os
import requests

class Notifer(object):
    """
    Notifer Object
    :member notify_token:
    """
    def __init__(self,notify_token):
        """
        __init__
        :param notify_token:
        Your LineNotify Acess Token

        """
        self.notify_token=notify_token

    def send_message( self,string):
        """
        A function that notifies LINENotify of the character string given as an argument
        :param string:
            A string to be notified
        :return response:
        """
        url = 'https://notify-api.line.me/api/notify'
        header = {'Authorization': 'Bearer ' + self.notify_token}
        payload = {'message': string}
        res = requests.post ( url, data=payload, headers=header )
        return str ( res )

def send_message(token,string):
    """
    A function that notifies LINENotify of the character string given as an argument
    :param string:
        A string to be notified
    :param token:
        LineNotifyToken
    :return response:
    """
    url = 'https://notify-api.line.me/api/notify'
    header = {'Authorization': 'Bearer ' + token}
    payload = {'message': string}
    res = requests.post ( url, data=payload, headers=header )
    return str ( res )


