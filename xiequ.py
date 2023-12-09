#!/bin/python
# -*- coding: utf-8 -*-
"""
自动更新携趣的IP白名单
Author： 为了你不敢懈怠
last_update: 20231201

1.脚本放置在scripts根目录下，新建任务task update_xqwhitelist.py
2.配置环境变量，携趣白名单菜单查看自己的uid和ukey
export xiequ_uid='123456'
export xiequ_ukey='81BE18CA69E491EB473FF60D59123456'

"""
import requests
import os

# 获取环境变量
xiequ_uid = os.environ.get("xiequ_uid")
xiequ_ukey = os.environ.get("xiequ_ukey")
if xiequ_uid is None:
    print("环境变量 xiequ_uid 不存在，请设置后重新运行程序")
    exit()

if xiequ_ukey is None:
    print("环境变量 xiequ_ukey 不存在，请设置后重新运行程序")
    exit()

def get_public_ip():
    try:
        response = requests.get('https://ipinfo.io')
        data = response.json()
        return data['ip']
    except requests.exceptions.RequestException as e:
        print('获取公网 IP 地址时出错:', str(e))

def get_whitelist_ip():
    try:
        url = f'http://op.xiequ.cn/IpWhiteList.aspx?uid={xiequ_uid}&ukey={xiequ_ukey}&act=get'
        response = requests.get(url)
        data = response.text
        return data
    except requests.exceptions.RequestException as e:
        print('获取白名单 IP 地址时出错:', str(e))

# 获取公网 IP 地址
public_ip = get_public_ip()
print('当前的公网 IP 地址是:', public_ip)

# 获取白名单 IP 地址
whitelist_ip = get_whitelist_ip()
print('当前的白名单 IP 地址是:', whitelist_ip)

# 比较公网 IP 和白名单 IP
if public_ip and whitelist_ip and public_ip != whitelist_ip:
    # 添加新 IP 地址
    add_url = f'http://op.xiequ.cn/IpWhiteList.aspx?uid={xiequ_uid}&ukey={xiequ_ukey}&act=add&ip={public_ip}'
    add_response = requests.get(add_url)
    print('添加新 IP 地址:', add_response.text)

    # 删除旧 IP 地址
    del_url = f'http://op.xiequ.cn/IpWhiteList.aspx?uid={xiequ_uid}&ukey={xiequ_ukey}&act=del&ip={whitelist_ip}'
    del_response = requests.get(del_url)
    print('删除旧 IP 地址:', del_response.text)
else:
    print('公网 IP 与白名单 IP 一致，无需进行调整')
