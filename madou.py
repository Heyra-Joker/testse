import itertools
import string

import hashlib
import base64
import urllib.parse


def get_signed_url_parameter(cdn_resource_url: str, file_path: str, secure_token: str,
                             expiry_timestamp: str) -> str:
    # # 在文件路径开头添加斜杠（如果缺少）
    # if not file_path.startswith('/'):
    #     file_path = '/' + file_path

    # # 从文件路径中去掉查询字符串
    # position_of_start_query = file_path.find('?')
    # if position_of_start_query != -1:
    #     file_path = file_path[:position_of_start_query]

    # 构建哈希字符串
    hash_value = file_path + secure_token
    # expiry_str = ''

    if expiry_timestamp:
        hash_value = expiry_timestamp + hash_value
        # expiry_str = f',{expiry_timestamp}'

    # 生成MD5哈希并替换无效字符
    md5_hash = hashlib.md5(hash_value.encode('utf-8')).digest()
    final_hash = base64.b64encode(md5_hash).decode('utf-8').replace('+', '-').replace('/', '_')

    # 返回完整的URL
    # return f'https://{cdn_resource_url}{file_path}?secure={final_hash}{expiry_str}'
    return final_hash


def generate_strings(n: int):
    characters = string.ascii_letters + string.digits + string.punctuation  # You can add more characters if needed
    for p in itertools.product(characters, repeat=n):
        yield ''.join(p)


# 示例用法
cdn_url = "example.cdn.com"
file_path = "video.mp4"
expiry_timestamp = "1692949460"  # 可选的到期时间戳
# target_secure = "https://eden.modelmediaasia.com/asia/MD-0288.mp4?secure=yP2FmKwolWvY68B_tcjoRw==,1724511497"
target_secure = "yP2FmKwolWvY68B_tcjoRw=="
# Example usage: generate all strings of length 8
for length in range(8, 65):
    print(length, "start")
    for secure_token in generate_strings(length):
        secure = get_signed_url_parameter(cdn_url, file_path, secure_token, expiry_timestamp)
        if secure == target_secure:
            print(secure_token)
            exit(0)
