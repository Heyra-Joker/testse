# -*- encoding: utf-8 -*-

import requests

cookies = {
    'user': 'QZ-joker030-09069e954c91cceaea07ed693ed721fe'
}

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://19jtv.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://19jtv.com',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
    'username2': "''; SELECT *",
    'password2': "?",
}

proxy = {
    # 'http': 'http://127.0.0.1:7890',
    # 'https': 'http://127.0.0.1:7890',
}
response = requests.get('https://19jtv.com/category/cn/16159', cookies=cookies, headers=headers,  proxies=proxy)

print(response.text)
