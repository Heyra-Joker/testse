# -*- encoding: utf-8 -*-
from starlette import requests

cookies = {
    '_ga': 'GA1.1.1195164822.1720351273',
    '__utma': '50351329.1195164822.1720351273.1722739866.1722739866.1',
    '__utmb': '50351329.0.10.1722739866',
    '__utmc': '50351329',
    '__utmz': '50351329.1722739866.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'cf_clearance': 'ilZl2woUbLUeIrTxB2hdaqmhSjaWu4fee2FZAtigdD4-1722739866-1.0.1.1-MYmG9LoWUGBo1Yvw1AydJihL3Ia86RSrfwMQA6cG9q4IW86l1x_GfCmP8lYCRAZFAyzdOM8_P9omTEt5blIOSg',
    'CLIPSHARE': '5851c7ab85e959335d290e3fbd2728ad',
    '_ga_K5S02BRGF0': 'GS1.1.1722739868.2.1.1722741440.0.0.0',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': '_ga=GA1.1.1195164822.1720351273; __utma=50351329.1195164822.1720351273.1722739866.1722739866.1; __utmb=50351329.0.10.1722739866; __utmc=50351329; __utmz=50351329.1722739866.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); cf_clearance=ilZl2woUbLUeIrTxB2hdaqmhSjaWu4fee2FZAtigdD4-1722739866-1.0.1.1-MYmG9LoWUGBo1Yvw1AydJihL3Ia86RSrfwMQA6cG9q4IW86l1x_GfCmP8lYCRAZFAyzdOM8_P9omTEt5blIOSg; CLIPSHARE=5851c7ab85e959335d290e3fbd2728ad; _ga_K5S02BRGF0=GS1.1.1722739868.2.1.1722741440.0.0.0',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://www.91porn.com/index.php',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}

params = {
    'viewkey': '213717286',
    'c': 'f7ugg',
    'viewtype': '',
    'category': '',
}

proxy = {
    'http': 'http://127.0.0.1:7890',
    'https': 'http://127.0.0.1:7890',
}
response = requests.get('https://www.91porn.com/view_video.php?viewkey=213717286&c=f7ugg&viewtype=&category=', cookies=cookies, headers=headers,
                        proxies=proxy)

print(response.text)
