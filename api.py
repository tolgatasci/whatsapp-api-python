import requests


class Api:
    device_token = ""
    base_url = "https://whatsapp.securedatainfo.com/api/"

    def __init__(self, device_token=False):
        if device_token:
            self.device_token = device_token

    def GET(self, method, params=dict()):
        if "token" not in params:
            params['token'] = self.device_token
        resp = requests.get(url=self.base_url + method, params=params)
        if resp.status_code != 200:
            raise ValueError('404')
        return resp.json()

    def POST(self, method, data={}, files=None):
        if "token" not in data:
            data['token'] = self.device_token
        if not files:
            resp = requests.post(self.base_url + method, data=data)
            return resp.json()
        else:
            resp = requests.post(self.base_url + method, files=files, data=data)
            return resp.json()

    def messages(self, page=1, limit=20, phone=None, status=None):
        try:
            params = dict(
                page=page,
                limit=limit,
                status=status,
                phone=phone
            )
            return self.GET(method="message/list", params=params)
        except Exception as error:
            return str(error)

    def incoming_messages(self, page=1, limit=20, phone=None):
        try:
            params = dict(
                page=page,
                limit=limit,
                phone=phone
            )
            return self.GET(method="message/incoming", params=params)
        except Exception as error:
            return str(error)

    def show_message(self, message_id=None):
        try:
            return self.GET(method="message/{message_id}/show".format(message_id=message_id))
        except Exception as error:
            return str(error)

    def send_message(self, message_body=None, phone_numbers={}, files=None):
        try:
            if not isinstance(phone_numbers, list):
                raise ValueError('phone_numbers required array')
            data = {
                "message_body": message_body
            }

            for idx, phone in enumerate(phone_numbers):
                data["phone_numbers[" + str(idx) + "][phone]"] = phone['phone']
                if 'message' in phone:
                    data["phone_numbers[" + str(idx) + "][message]"] = phone['message']
            return self.POST(method="message/send", data=data, files=files)
        except Exception as error:
            return str(error)

    def send_code(self, code=None, phone=""):
        try:
            data = {
                "code": code,
                "phone_number": phone
            }
            return self.POST(method="message/send_code", data=data)
        except Exception as error:
            return str(error)

    def info(self):
        try:

            return self.GET(method="user/info")
        except Exception as error:
            return str(error)