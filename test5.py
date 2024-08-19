# -*- encoding: utf-8 -*-
import base64
import hashlib

import requests

cookies = {
    'uid': '171828796601',
}

headers = {
    'Host': 'hj2404cca5.top',
    # 'X-User-Id': '171828796601',
    # 'Cookie': 'uid=171828796601',
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json',
    'Sec-Fetch-Site': 'same-origin',
    'ContentType': 'application/json',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'X-User-Token': 'null',
    'Sec-Fetch-Mode': 'cors',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Access-Control-Allow-Credentials': 'true',
    'Origin': 'https://hj2404cca5.top',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1',
    'Referer': 'https://hj2404cca5.top/login',
    # 'Content-Length': '146',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    # 'mVer': '211112203214',
}

json_data = {
    'username': '447592774@qq.com',
    'password': 'woaij100',
    'captchaCode': '',
    'captchaId': '',
    'ref': "",
    'sign': '',

}

sign = hashlib.md5(f"{json_data['username']}{json_data['password']}{headers['User-Agent']}".encode()).hexdigest()
print(sign)
json_data['sign'] = sign

response = requests.post('https://hj2404cca5.top/api/login/signin', json=json_data, headers=headers)
print(response.request.body.decode())
print(response.text)
# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
# data = '{"username":"jokermonster030@gmail.com","password":"woaij100","captchaCode":"","captchaId":"","ref":"/","sign":"93aff38409dc61adf9248e175f01e5c7"}'
# response = requests.post('https://hj2404cca5.top/api/login/signin', cookies=cookies, headers=headers, data=data)
data = response.json()["data"]
atob_data_1 = base64.urlsafe_b64decode(data.encode())
atob_data_2 = base64.urlsafe_b64decode(atob_data_1)
atob_data_3 = base64.urlsafe_b64decode(atob_data_2)
print(atob_data_3.decode())


# {"isEncrypted":false,"errorCode":0,"message":"用户不存在","success":false,"data":null}