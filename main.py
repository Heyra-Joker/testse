import hashlib
import time

from urllib.parse import quote_plus

import requests

from sign import Sign

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'origin': 'https://4096se.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://4096se.com/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

# url = "/api/v1?t=1719112802&url=http%3A%2F%2Fa"

url = quote_plus("https://haijiao.com/post/details?pid=1385094")
print(url)
t = int(time.time())
# t = "1719124242"
uri = f"/api/v1?t={t}&url={url}"
s = Sign()
sign_ = s.run(uri)
print(sign_)
req_url = "https://api.4096se.com" + uri + f"&sign={sign_}"
print(req_url)
proxy = {
    'http': 'http://127.0.0.1:7890',
    'https': 'http://127.0.0.1:7890'
}
response = requests.get(
    req_url,
    headers=headers,
    # proxies=proxy
)
print(response.text)
