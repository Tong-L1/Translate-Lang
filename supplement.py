import json


def getkey(file_json):
    return [str(i) for i in file_json]


def getnotin():
    enkey = getkey(enjson)
    zhkey = getkey(zhjson)
    notin = []
    for i in enkey:
        if i not in zhkey:
            notin.append(i)
            # print(i)
    return notin


def getinen():
    jsonstr = '{\n'
    count = 0
    for i in enjson:
        if i in notin:
            jsonstr += '"' + i + '":"' + enjson.get(i).replace('"',"'") + '"'
            if count < len(notin) - 1:
                jsonstr += ','
            jsonstr += '\n'
            count += 1
    jsonstr += '}'
    return jsonstr


en = open('lang/en_us.json', 'r', encoding='utf-8')
zh = open('lang/zh_cn.json', 'r', encoding='utf-8')
enjson = json.load(en)
zhjson = json.load(zh)
en.close()
zh.close()
notin = getnotin()
jsonstr = getinen()
zn_file = open('lang/new.json', 'w', encoding='utf-8')
zn_file.write(json.loads(json.dumps(jsonstr, indent=1, ensure_ascii=False)))
zn_file.close()
