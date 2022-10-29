# -*- coding: utf-8 -*-

# This code shows an example of text translation from English to Simplified-Chinese.
# This code runs on Python 2.7.x and Python 3.x.
# You may install `requests` to run this code: pip install requests
# Please refer to `https://api.fanyi.baidu.com/doc/21` for complete api document

import requests
import random
import json
from hashlib import md5
from time import sleep


# Generate salt and sign
def make_md5(s, encoding='utf-8'):
    return md5(s.encode(encoding)).hexdigest()


def translate(query):
    # Set your own appid/appkey.
    appid = '你的appid'
    appkey = '你的appkey'

    # For list of language codes, please refer to `https://api.fanyi.baidu.com/doc/21`
    from_lang = 'en'
    to_lang = 'zh'

    endpoint = 'http://api.fanyi.baidu.com'
    path = '/api/trans/vip/translate'
    url = endpoint + path

    salt = random.randint(32768, 65536)
    sign = make_md5(appid + query + str(salt) + appkey)

    # Build request
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'appid': appid, 'q': query, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}

    # Send request
    r = requests.post(url, params=payload, headers=headers)
    result = r.json()
    sleep(0.1)
    return result


def getvalue(file_json):
    return [str(file_json.get(i)) for i in file_json]


def writezh(file_json, en, zn):
    j = 0
    str1 = str(file_json).replace("'", '"')
    # print(new_json)
    en_len = en.__len__()
    while j < en_len:
        str1 = str1.replace(en[j], zn[j])
        j += 1

    new_json = json.loads(str1)
    # print(json.dumps(new_json, indent=en_len, ensure_ascii=False))
    zn_file = open('lang/zn_ch.json', 'w', encoding='utf-8')
    zn_file.write(json.dumps(new_json, indent=1, ensure_ascii=False))
    zn_file.close()


with open('lang/en_us.json', encoding='utf-8') as a:
    file_json = json.load(a)
    en = getvalue(file_json)
    zn = []
    len = len(en)
    for i in range(len):
        zn.append(translate(en[i])['trans_result'][0]['dst'])
        print(str(i)+"/"+str(len))
    writezh(file_json, en, zn)

