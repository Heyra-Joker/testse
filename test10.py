import requests

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    # 'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo0MTQ4OCwiY2FtcGFpZ25faWQiOjAsImV4cCI6MTcyNTExMjIzMSwiaWF0IjoxNzI0NTA3NDMxfQ.IrvHLv67G2LlOqwcPcVTeSQTPcbfa_zpFznycxexyq0',
    'cache-control': 'no-cache',
    'origin': 'https://modelmediaasia.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://modelmediaasia.com/',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
}

proxy = {
    'http': 'http://127.0.0.1:7890',
    'https': 'http://127.0.0.1:7890',
}
response = requests.get('https://api.modelmediaasia.com/api/v2/videos/MD-0288', headers=headers, proxies=proxy).json()

data = response['data']
print(data)


