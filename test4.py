# -*- encoding: utf-8 -*-
import base64
import json

import requests

cookies = {
    'mainshow': 'true',
    'token': 'a7fab89326c041769dc13afd547da2ef',
    'uid': '171828796601',
}

headers = {
    'Host': 'hj2404cca5.top',
    # 'Cookie': 'mainshow=true; token=a7fab89326c041769dc13afd547da2ef; uid=171828796601',
    # 'Accept': 'application/json, text/plain, */*',
    # 'Content-Type': 'application/json;charset=utf-8',
    # 'Sec-Fetch-Site': 'same-origin',
    # 'ContentType': 'application/json',
    # 'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    # 'Sec-Fetch-Mode': 'cors',
    # # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Access-Control-Allow-Credentials': 'true',
    # 'Origin': 'https://hj2404cca5.top',
    # 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1',
    # 'Referer': 'https://hj2404cca5.top/post/details?pid=1160308',
    # # 'Content-Length': '77',
    # 'Connection': 'keep-alive',
    # 'Sec-Fetch-Dest': 'empty',
    # 'mVer': '211112203214',
    # 'X-User-Id': '171828796601',
    # 'X-User-Token': '1bbc65fed211411e8c2366b36de97a54',
    # 'X-Client-Ip': '37.128.255.5',
}

json_data = {
    # 'id': 7036624,
    'id': 8837981,
    # 'resource_id': 1160308,
    'resource_id': 1463184,
    'resource_type': 'topic',
    'line': '',
}

proxy = {
    # 'http': 'http://127.0.0.1:7890',
    # 'https': 'http://127.0.0.1:7890',
}
response = requests.post('https://haijiao.pro/api/attachment', headers=headers, json=json_data, verify=False, proxies=proxy)
print(response.request.body.decode('utf-8'))
print(response.text)
topic_data = response.json()
data = topic_data['data']
if not data:
    exit(0)
# 解密
atob_data_1 = base64.urlsafe_b64decode(data.encode())
atob_data_2 = base64.urlsafe_b64decode(atob_data_1)
atob_data_3 = base64.urlsafe_b64decode(atob_data_2)
print(atob_data_3.decode())
data2 = json.loads(atob_data_3.decode())
print("https://hj2404cca5.top" + data2['remoteUrl'])
# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
# data = '{"id":7036624,"resource_type":"topic","resource_id":1160308,"line":"normal2"}'
# response = requests.post('https://hj2404cca5.top/api/attachment', cookies=cookies, headers=headers, data=data)
#
#
# reqURL = "https://hj2404cca5.top" + data2['remoteUrl']
#
# resp = requests.get(reqURL)
# print(resp.text)
