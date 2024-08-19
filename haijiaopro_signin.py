# -*- encoding: utf-8 -*-
import requests

cookies = {
    '_ga': 'GA1.1.1083277715.1723979148',
    'NOTLOGIN': 'NOTLOGIN',
    '_cfuvid': 'svGWvcGdB6cc3M8h86MPRgxfz2lud__J8i1r5Fx.dzY-1723984155000-0.0.1.1-604800000',
    '_ga_Y2CH3RXB10': 'GS1.1.1723979147.1.1.1723984158.0.0.0',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    # 'cookie': '_ga=GA1.1.1083277715.1723979148; NOTLOGIN=NOTLOGIN; _cfuvid=svGWvcGdB6cc3M8h86MPRgxfz2lud__J8i1r5Fx.dzY-1723984155000-0.0.1.1-604800000; _ga_Y2CH3RXB10=GS1.1.1723979147.1.1.1723984158.0.0.0',
    'origin': 'https://haijiao.pro',
    'pcver': '2',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://haijiao.pro/login',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}

json_data = {
    'username': '447592774',
    'password': '447592774',
    'referid': None,
    'locked': '0',
}

response = requests.post('https://haijiao.pro/api/login/signin',  headers=headers, json=json_data)
print(response.text)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"username":"447592774","password":"447592774","referid":null,"locked":"1"}'
#response = requests.post('https://haijiao.pro/api/login/signin', cookies=cookies, headers=headers, data=data)