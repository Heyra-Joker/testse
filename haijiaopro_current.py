import time

import requests

cookies = {
    '_ga': 'GA1.1.1823280214.1723554309',
    '_cfuvid': 'PHZsiY7z5E725PhVv9NJfAa.Ud9Pqon4FIqn.0pmxDI-1724078759687-0.0.1.1-604800000',
    'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiaHd3ZXJ3ZSIsImlkIjozMTE3NTcxLCJpYXQiOjE3MjQwNzg3NjgsImV4cCI6MTczMjcxODc2OH0.-7mTVheLp7uULGnoKZeGmNmDCf3AHqbt9_My8Qd7i6s',
    'uid': '3117571',
    '_ga_Y2CH3RXB10': 'GS1.1.1724078232.3.1.1724078781.0.0.0',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': '_ga=GA1.1.1823280214.1723554309; _cfuvid=PHZsiY7z5E725PhVv9NJfAa.Ud9Pqon4FIqn.0pmxDI-1724078759687-0.0.1.1-604800000; token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiaHd3ZXJ3ZSIsImlkIjozMTE3NTcxLCJpYXQiOjE3MjQwNzg3NjgsImV4cCI6MTczMjcxODc2OH0.-7mTVheLp7uULGnoKZeGmNmDCf3AHqbt9_My8Qd7i6s; uid=3117571; _ga_Y2CH3RXB10=GS1.1.1724078232.3.1.1724078781.0.0.0',
    'pcver': '2',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://haijiao.pro/personal/wallet',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'x-user-id': '3117571',
    'x-user-token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiaHd3ZXJ3ZTIiLCJpZCI6MzEyNTcwNSwiaWF0IjoxNzI0MjMxOTU5LCJleHAiOjE3MzI4NzE5NTl9.3tRQlT1H57m9Iqt7ZJTfGeyZHJu5533YnM0nGRVEXOE'
}

params = {
    'date': str(int(time.time() * 1000)),
}

response = requests.get('https://haijiao.pro/api/user/current', params=params, headers=headers)
print(response.text)

# diamond