"""
@Auth ： LTX-Name
@File ：xqip.py
"""

import requests

# 进入携趣白名单页面，下面接口查看自己的uid和ukey，替换下面的值即可
uid = 105964
ukey = "AAE42581AA0F57EC6B601F9DCECD1C9D"


def query_exist_ip(uid, ukey):
    url = f"http://op.xiequ.cn/IpWhiteList.aspx?uid={uid}&ukey={ukey}&act=get"

    payload = {}
    headers = {
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
        'Accept': '*/*',
        'Host': 'op.xiequ.cn',
        'Connection': 'keep-alive'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response = response.text.split(",")
    global ip
    ip = response[0]
    print(f"当前白名单第一个ip为{ip}")


def del_exist_ip(uid, ukey):
    url = f"http://op.xiequ.cn/IpWhiteList.aspx?uid={uid}&ukey={ukey}&act=del&ip={ip}"

    payload = {}
    headers = {
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
        'Accept': '*/*',
        'Host': 'op.xiequ.cn',
        'Connection': 'keep-alive',
        'Cookie': 'acw_tc=7ae4c3a816868379583228477e4119c2921e7d77ace180c63caf6ccd45'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    print(f"删除白名单第一个ip结果：{response.text}")


def query_local_ip(uid, ukey):
    global ip
    response = requests.get('https://api.ipify.org/?format=json')
    ip = response.json()['ip']
    print(f"本机当前ip为：{ip}")


def add_local_ip(uid, ukey):
    url = f"http://op.xiequ.cn/IpWhiteList.aspx?uid={uid}&ukey={ukey}&act=add&ip={ip}"

    payload = {}
    headers = {
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
        'Accept': '*/*',
        'Host': 'op.xiequ.cn',
        'Connection': 'keep-alive'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    r = response.text
    print(f"添加本机ip进白名单结果:{r}")


query_exist_ip(uid, ukey)
del_exist_ip(uid, ukey)
query_local_ip(uid, ukey)
add_local_ip(uid, ukey)
