# coding:UTF-8
import requests

URL = 'https://notify-api.line.me/api/notify'


class Notifer(object):
    """
    Notifer Object
    :member notify_token:
    """

    def __init__(self, notify_token: str):
        """
        __init__
        :param notify_token:
        Your LineNotify Acess Token

        """
        self.notify_token = notify_token

    def send_message(self, message: str) -> str:
        """
        A function that notifies LINENotify of the character string given as an argument

        :param message:
            A string to be notified

        :return response:
            server response (thats like 200 etc...)
        """
        headers = {'Authorization': 'Bearer ' + self.notify_token}
        payload = {'message': message}
        res = requests.post(URL, data=payload, headers=headers)
        return str(res)

    def send_sticker_with_message(self, message: str, sticker_package_id: str, sticker_id: str) -> str:
        """
        if you want to know what i can use, you will see https://devdocs.line.me/files/sticker_list.pdf
        :param message:
            A string to be notified
        :param sticker_package_id:
        :param sticker_id:
        :return response:
            server response (thats like 200 etc...)
        """

        payload = {'message': message, 'stickerPackageId': sticker_package_id, 'stickerId': sticker_id}
        headers = {'Authorization': 'Bearer ' + self.notify_token}  # 発行したトークン
        res = requests.post(URL, data=payload, headers=headers)
        return str(res)

    def send_photo_with_message(self, message: str, path: str) -> str:
        """
        You can send .png .jpg type message.
        Notice: You have to write message.
        :param message:
        :param path:
            File pass (relative)
        :return response:
            server response (thats like 200 etc...)
        """
        payload = {"message": message}
        headers = {"Authorization": "Bearer " + self.notify_token}
        files = {"imageFile": open(path, "rb")}
        res = requests.post(URL, data=payload, headers=headers, files=files)
        return str(res)


def send_message(token, message: str) -> str:
    """
    A function that notifies LINENotify of the character string given as an argument
    :param message:
        A string to be notified
    :param token:
        LineNotify Access Token
    :return response:
        server response (thats like 200 etc...)
    """
    notify = Notifer(token)
    return notify.send_message(message)


def send_sticker_with_message(token, message: str, sticker_package_id: str, sticker_id: str) -> str:
    """
    if you want to know what i can use, you will see https://devdocs.line.me/files/sticker_list.pdf

    :param token:
        LineNotify Access Token
    :param message:
        A string to be notified
    :param sticker_package_id:
    :param sticker_id:
    :return response:
        server response (thats like 200 etc...)
    """
    notify = Notifer(token)
    return notify.send_sticker_with_message(message, sticker_package_id, sticker_id)


def send_photo_with_message(token: str, message: str, path: str) -> str:
    """
    You can send .png .jpg type message.
    Notice: You have to write message.
    :param token:
        LineNotify Access Token
    :param message:
    :param path:
        File pass (relative)

    :return response:
        server response (thats like 200 etc...)
    """
    notify = Notifer(token)
    return notify.send_photo_with_message(message, path)
