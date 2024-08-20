# -*- encoding: utf-8 -*-

import requests

cookies = {
    '_ga': 'GA1.1.771992626.1722610140',
    '_cfuvid': '01vgvui6l0a_fQSrRCuT6jY5WIhyuKEEFbOOyCIOlxA-1722611304540-0.0.1.1-604800000',
    'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiaHV3YW5nMSIsImlkIjozMDI2NDc0LCJpYXQiOjE3MjI2MTEzMDgsImV4cCI6MTczMTI1MTMwOH0.kxbbACNNi2jFsm293-R7D7UHKeD84JU2NJKJ5WBpykg',
    'uid': '3026474',
    'user': '%7B%22id%22%3A3026474%2C%22nickname%22%3A%22%u6D77%u89D2-3026474%22%2C%22avatar%22%3A%220%22%2C%22description%22%3A%22%22%2C%22topicCount%22%3A0%2C%22videoCount%22%3A0%2C%22commentCount%22%3A0%2C%22fansCount%22%3A0%2C%22favoriteCount%22%3A0%2C%22status%22%3A0%2C%22sex%22%3A0%2C%22vip%22%3A0%2C%22vipExpiresTime%22%3A%220001-01-01%2000%3A00%3A00%22%2C%22certified%22%3Afalse%2C%22certVideo%22%3Afalse%2C%22certProfessor%22%3Afalse%2C%22famous%22%3Afalse%2C%22forbidden%22%3Afalse%2C%22tags%22%3Anull%2C%22role%22%3A0%2C%22diamondConsume%22%3A0%2C%22title%22%3A%7B%22id%22%3A0%2C%22name%22%3A%22%22%2C%22consume%22%3A0%2C%22consumeEnd%22%3A0%2C%22icon%22%3A%22/imgs/headicon/usertitle4.png%22%7D%2C%22friendStatus%22%3Afalse%2C%22voiceStatus%22%3Afalse%2C%22videoStatus%22%3Afalse%2C%22voiceMoneyType%22%3A0%2C%22voiceAmount%22%3A0%2C%22videoMoneyType%22%3A0%2C%22videoAmount%22%3A0%2C%22depositMoney%22%3A0%2C%22phone%22%3A%22%22%2C%22userBank%22%3Anull%2C%22parentId%22%3A0%2C%22gold%22%3A0%2C%22diamond%22%3A50%2C%22passwordSet%22%3Atrue%2C%22payPasswordSet%22%3Afalse%2C%22popularity%22%3A10%2C%22topicLikeNum%22%3A0%2C%22bindUser%22%3A%22%22%2C%22username%22%3A%22abc%22%2C%22email%22%3A%22%22%2C%22emailVerified%22%3Afalse%2C%22createTime%22%3A%220001-01-01%2000%3A00%3A00%22%2C%22lastLoginTime%22%3A%220001-01-01%2000%3A00%3A00%22%2C%22lastLoginIp%22%3A%22%22%2C%22certifiedExpired%22%3Afalse%2C%22certProfessorExpired%22%3Afalse%2C%22certVideoExpired%22%3Afalse%7D',
    '_ga_Y2CH3RXB10': 'GS1.1.1722652156.2.1.1722652348.0.0.0',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': '_ga=GA1.1.771992626.1722610140; _cfuvid=01vgvui6l0a_fQSrRCuT6jY5WIhyuKEEFbOOyCIOlxA-1722611304540-0.0.1.1-604800000; token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiaHV3YW5nMSIsImlkIjozMDI2NDc0LCJpYXQiOjE3MjI2MTEzMDgsImV4cCI6MTczMTI1MTMwOH0.kxbbACNNi2jFsm293-R7D7UHKeD84JU2NJKJ5WBpykg; uid=3026474; user=%7B%22id%22%3A3026474%2C%22nickname%22%3A%22%u6D77%u89D2-3026474%22%2C%22avatar%22%3A%220%22%2C%22description%22%3A%22%22%2C%22topicCount%22%3A0%2C%22videoCount%22%3A0%2C%22commentCount%22%3A0%2C%22fansCount%22%3A0%2C%22favoriteCount%22%3A0%2C%22status%22%3A0%2C%22sex%22%3A0%2C%22vip%22%3A0%2C%22vipExpiresTime%22%3A%220001-01-01%2000%3A00%3A00%22%2C%22certified%22%3Afalse%2C%22certVideo%22%3Afalse%2C%22certProfessor%22%3Afalse%2C%22famous%22%3Afalse%2C%22forbidden%22%3Afalse%2C%22tags%22%3Anull%2C%22role%22%3A0%2C%22diamondConsume%22%3A0%2C%22title%22%3A%7B%22id%22%3A0%2C%22name%22%3A%22%22%2C%22consume%22%3A0%2C%22consumeEnd%22%3A0%2C%22icon%22%3A%22/imgs/headicon/usertitle4.png%22%7D%2C%22friendStatus%22%3Afalse%2C%22voiceStatus%22%3Afalse%2C%22videoStatus%22%3Afalse%2C%22voiceMoneyType%22%3A0%2C%22voiceAmount%22%3A0%2C%22videoMoneyType%22%3A0%2C%22videoAmount%22%3A0%2C%22depositMoney%22%3A0%2C%22phone%22%3A%22%22%2C%22userBank%22%3Anull%2C%22parentId%22%3A0%2C%22gold%22%3A0%2C%22diamond%22%3A50%2C%22passwordSet%22%3Atrue%2C%22payPasswordSet%22%3Afalse%2C%22popularity%22%3A10%2C%22topicLikeNum%22%3A0%2C%22bindUser%22%3A%22%22%2C%22username%22%3A%22abc%22%2C%22email%22%3A%22%22%2C%22emailVerified%22%3Afalse%2C%22createTime%22%3A%220001-01-01%2000%3A00%3A00%22%2C%22lastLoginTime%22%3A%220001-01-01%2000%3A00%3A00%22%2C%22lastLoginIp%22%3A%22%22%2C%22certifiedExpired%22%3Afalse%2C%22certProfessorExpired%22%3Afalse%2C%22certVideoExpired%22%3Afalse%7D; _ga_Y2CH3RXB10=GS1.1.1722652156.2.1.1722652348.0.0.0',
    'pcver': '2',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://haijiao.pro/post/details?pid=494259',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    # 'x-user-id': '3026417',
    'x-user-token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiNDQ3NTkyNzc0IiwiaWQiOjMwMjY0MTcsImlhdCI6MTcyMzk4NDE2MiwiZXhwIjoxNzMyNjI0MTYyfQ.HxWvEr48DYlI0uBAbUOwubx5tQk8qzsJmbDroEgKbcs'
}

proxy = {
    'http': 'http://127.0.0.1:7890',
    'https': 'http://127.0.0.1:7890',
}
response = requests.get('https://haijiao.pro/api/topic/63566', proxies=proxy, headers=headers)
print(response.text)

# 666888
# is_buy