import requests

cookies = {
    '_ga': 'GA1.1.1823280214.1723554309',
    '_cfuvid': 'PHZsiY7z5E725PhVv9NJfAa.Ud9Pqon4FIqn.0pmxDI-1724078759687-0.0.1.1-604800000',
    'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiaHd3ZXJ3ZSIsImlkIjozMTE3NTcxLCJpYXQiOjE3MjQwNzg3NjgsImV4cCI6MTczMjcxODc2OH0.-7mTVheLp7uULGnoKZeGmNmDCf3AHqbt9_My8Qd7i6s',
    'uid': '3117571',
    '_ga_Y2CH3RXB10': 'GS1.1.1724078232.3.1.1724079089.0.0.0',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    # 'cookie': '_ga=GA1.1.1823280214.1723554309; _cfuvid=PHZsiY7z5E725PhVv9NJfAa.Ud9Pqon4FIqn.0pmxDI-1724078759687-0.0.1.1-604800000; token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiaHd3ZXJ3ZSIsImlkIjozMTE3NTcxLCJpYXQiOjE3MjQwNzg3NjgsImV4cCI6MTczMjcxODc2OH0.-7mTVheLp7uULGnoKZeGmNmDCf3AHqbt9_My8Qd7i6s; uid=3117571; _ga_Y2CH3RXB10=GS1.1.1724078232.3.1.1724079089.0.0.0',
    'origin': 'https://haijiao.pro',
    'pcver': '2',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://haijiao.pro/post/details?pid=1054425',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'x-user-id': '3117571',
    'x-user-token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiaHd3ZXJ3ZSIsImlkIjozMTE3NTcxLCJpYXQiOjE3MjQwNzg3NjgsImV4cCI6MTczMjcxODc2OH0.-7mTVheLp7uULGnoKZeGmNmDCf3AHqbt9_My8Qd7i6s',
}

json_data = {
    'topic_id': 45997,
}

# 购买接口, 注意可以重复购买
response = requests.post('https://haijiao.pro/api/topic/buy/sell',  headers=headers, json=json_data)
print(response.text)

# {"isEncrypted":false,"errorCode":0,"message":"","success":true,"data":null}

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"topic_id":1054425}'
#response = requests.post('https://haijiao.pro/api/topic/buy/sell', cookies=cookies, headers=headers, data=data)