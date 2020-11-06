import requests
import hashlib
import config


class LoginAndHeader:
    def get_token(self):
        password = hashlib.md5(config.PASSWORD.encode(encoding='utf-8')).hexdigest()
        url = config.HOST + '/api/auth/account/login'

        header = {
            'Content-Type': 'application/json; charset=utf-8',
            "User-Agent": "PostmanRuntime/7.26.3",
        }

        data = {
            'name': config.USER,
            'password': password
        }

        res = requests.post(url, json=data, headers=header)
        try:
            assert 0 == res.json()['code']
            # print('token值为:', res.json()['data']['token'])
            return res.json()['data']['token']
        except Exception:
            # print(res.json())
            return res.json()

    def get_header(self):
        token = 'c_token=' + self.get_token()
        header = {
            'Content-Type': 'application/json; charset=utf-8',
            "User-Agent": "PostmanRuntime/7.26.3",
            'Cookie': token
        }
        return header


if __name__ == '__main__':
    print(LoginAndHeader().get_token())
    print(LoginAndHeader().get_header())
