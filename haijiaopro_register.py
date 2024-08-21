import requests

cookies = {
    '_ga': 'GA1.1.1823280214.1723554309',
    '_cfuvid': 'CQmLgsCwwk55TGcSV97s1GSr54NIIHk0fTxGxn0u.C4-1724078230485-0.0.1.1-604800000',
    '_ga_Y2CH3RXB10': 'GS1.1.1724078232.3.1.1724078265.0.0.0',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    # 'cookie': '_ga=GA1.1.1823280214.1723554309; _cfuvid=CQmLgsCwwk55TGcSV97s1GSr54NIIHk0fTxGxn0u.C4-1724078230485-0.0.1.1-604800000; _ga_Y2CH3RXB10=GS1.1.1724078232.3.1.1724078265.0.0.0',
    'origin': 'https://haijiao.pro',
    'pcver': '2',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://haijiao.pro/register',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}

json_data = {
    'username': 'hwwerwe2',
    'password': 'hwwerwe2',
    'rpassword': 'hwwerwe2',
    'referid': None,
    'locked': None,
}

proxy = {
    # "https": "http://127.0.0.1:7890",
    # "http": "http://127.0.0.1:7890"
}


response = requests.post('https://hjxx7.top/api/login/signup', headers=headers, json=json_data, proxies=proxy)
print(response.text)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"username":"hw83748","password":"hw83748","rpassword":"hw83748","referid":null,"locked":null}'
#response = requests.post('https://haijiao.pro/api/login/signup', cookies=cookies, headers=headers, data=data)