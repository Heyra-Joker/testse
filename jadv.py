# -*- encoding: utf-8 -*-

import requests

cookies = {
    'adult-warning-popup': 'disabled',
    'nats_cookie': 'https%253A%252F%252Ftheporndude.com%252F',
    'nats_sess': '20241f6fdfb7327c9db80abd87847ebd',
    'nats_landing': 'No%2BLanding%2BPage%2BURL',
    'locale': 'zh',
    'JAVSESSID': 'kqhinutjvtkp58rq1q15ife63q',
    'st_d': '%7B%7D',
    'feid': '2537118f3dd243f470a24d8988372ca1',
    'form_prices_zh': '1',
    'xfeid': '23a0c88ddeea10f604531f7c00f05522',
    'atas_uid': '',
    '_ym_uid': '172321115448487933',
    '_ym_d': '1723211154',
    '_ym_visorc': 'b',
    '_ym_isad': '2',
    'user_lang': 'zh',
    '_gcl_au': '1.1.1312379750.1723211171',
    'nats': 'NzAzLjIuMi4yLjAuMC4wLjAuMA',
    'utm': '%7B%22ads_type%22%3A%22%22%2C%22utm_type%22%3A%22organic%22%2C%22utm_source%22%3A%22google%22%7D',
    'sid': '01928d9cbfc2bce4d425af9e3fc1e981',
    'nats_unique': 'NzAzLjIuMi4yLjAuMC4wLjAuMA',
    'referer': 'https%3A%2F%2Fjavhd.com%2Fzh%2F',
    'jplayer__volume': '0.8',
    'last_visited_set': '18244',
    'feid_sa': '32',
    'sid_sa': '10',
}

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': 'adult-warning-popup=disabled; nats_cookie=https%253A%252F%252Ftheporndude.com%252F; nats_sess=20241f6fdfb7327c9db80abd87847ebd; nats_landing=No%2BLanding%2BPage%2BURL; locale=zh; JAVSESSID=kqhinutjvtkp58rq1q15ife63q; st_d=%7B%7D; feid=2537118f3dd243f470a24d8988372ca1; form_prices_zh=1; xfeid=23a0c88ddeea10f604531f7c00f05522; atas_uid=; _ym_uid=172321115448487933; _ym_d=1723211154; _ym_visorc=b; _ym_isad=2; user_lang=zh; _gcl_au=1.1.1312379750.1723211171; nats=NzAzLjIuMi4yLjAuMC4wLjAuMA; utm=%7B%22ads_type%22%3A%22%22%2C%22utm_type%22%3A%22organic%22%2C%22utm_source%22%3A%22google%22%7D; sid=01928d9cbfc2bce4d425af9e3fc1e981; nats_unique=NzAzLjIuMi4yLjAuMC4wLjAuMA; referer=https%3A%2F%2Fjavhd.com%2Fzh%2F; jplayer__volume=0.8; last_visited_set=18244; feid_sa=32; sid_sa=10',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://javhd.com',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    # 'sentry-trace': 'a6c60043b05548a8923dda41765f05ad-8b95c7dcd121ed6e-1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}

params = {
    'videoId': '113884',
    'is_trailer': '0',
}

proxy = {
    'http': 'http://127.0.0.1:7890',
    'https': 'http://127.0.0.1:7890',
}

response = requests.get('https://javhd.com/zh/player_api', params=params, proxies=proxy)
print(response.text)
