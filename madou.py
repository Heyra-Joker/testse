# -*- encoding: utf-8 -*-

import requests

headers = {
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://mddmp03.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://mddmp03.com/mobile/video',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
}
proxy = {
    'http': 'http://127.0.0.1:7890',
    'https': 'http://127.0.0.1:7890',
}



json_data = {
    'appId': 888,
    'pageNum': 1,
    'pageSize': 10,
    'type': 1,
}

response = requests.post('https://mddmp03.com/api/stat/landPageConfig/getByType', headers=headers, json=json_data, proxies=proxy, timeout=2)
print(response.text)