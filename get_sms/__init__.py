import requests
import json

__author__ = 'begyy'


class ParserSendMessage(object):
    __slots__ = ['phone_number', 'text', 'date_received', 'message_id', 'request_id', 'client_ip', 'user_id']

    def __init__(self, recipient, text, date_received, message_id, request_id, client_ip, user_id):
        self.phone_number = recipient
        self.text = text
        self.date_received = date_received
        self.message_id = message_id
        self.request_id = request_id
        self.client_ip = client_ip
        self.user_id = user_id


class ParserCheckStatus(object):
    __slots__ = ['phone_number', 'text', 'user_id', 'date_received', 'date_sent', 'date_delivered', 'message_id',
                 'request_id', 'status', 'count_messages', 'client_ip', 'description']

    def __init__(self, recipient, text, user_id, date_received, date_sent, date_delivered, message_id, request_id,
                 status, count_messages, client_ip, description):
        self.phone_number = recipient
        self.text = text
        self.user_id = user_id
        self.date_received = date_received
        self.date_sent = date_sent
        self.date_delivered = date_delivered
        self.message_id = message_id
        self.request_id = request_id
        self.status = status
        self.count_messages = count_messages
        self.client_ip = client_ip
        self.description = description


class Getsms:
    __slots__ = ['login', 'password', 'nickname', 'url', 'check_url', 'forbidden', 'forbidden_message']

    def __init__(self, login, password, nickname=None):
        self.login = login
        self.password = password
        self.nickname = nickname
        self.url = 'http://185.8.212.184/smsgateway/'
        self.check_url = f"{self.url}/status/"
        self.forbidden = 403
        self.forbidden_message = 'Скажите администратору чтобы дал вам доступ  http://getsms.uz/'

    def send_message(self, phone_numbers: list, text: str):
        '''
        >>> self.send_message(phone_numbers=['998998158172', '9989998157281'], text='Hello')
        '''
        messages = list()
        for phone_number in phone_numbers:
            messages.append(dict(
                phone=phone_number,
                text=text
            ))

        messages = json.dumps(messages)

        data = dict(
            login=self.login,
            password=self.password,
            nickname=self.nickname,
            data=messages
        )

        return self.response(self.url, data=data, parser=ParserSendMessage)

    def check_status(self, request_ids: list):
        '''
        >>> self.check_status(request_ids=[123456789])
        '''
        messages = list()
        for request_id in request_ids:
            messages.append(dict(
                request_id=request_id
            ))
        messages = json.dumps(messages)

        data = dict(
            login=self.login,
            password=self.password,
            nickname=self.nickname,
            data=messages
        )

        return self.response(self.check_url, data=data, parser=ParserCheckStatus)

    def response(self, url, data, parser):
        result = requests.post(url=url, json=data)
        if result.status_code != self.forbidden:
            results = result.json()
            if 'error' in results:
                return results

            objects = list()
            for result in results:
                objects.append(parser(**result))
            return objects
        return self.forbidden_message
