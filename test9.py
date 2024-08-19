import requests

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'origin': 'https://haijiao.pro',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://haijiao.pro/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}

while 1:
    response = requests.get('https://ts6.hjedd.pro/10/5ff7522618ffa32ac21e8b9c7960b1b8/8793662C3i9sx6t_i16.ts')
    print(response.text)