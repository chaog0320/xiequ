#携趣接口在 用户中心 白名单中获取 拉到最底下 白名单管理接口
#自行添加到青龙 等支持自动化任务面板  需支持python

import requests

def get_public_ip():
    try:
        # 使用一个返回你的外网IP地址的公共API
        response = requests.get('https://api.ipify.org/?format=json')
        data = response.json()
        public_ip = data['ip']
        return public_ip
    except Exception as e:
        return str(e)

def delete_all_from_ip_whitelist():
    try:
        # 构建请求URL来删除所有规则
	#写你的携趣删除白名单接口
	#示例 http://op.xiequ.cn/IpWhiteList.aspx?uid=XXXXX&ukey=XXXXXX&act=del&ip=all
        url = 'http://op.xiequ.cn/IpWhiteList.aspx?uid=105964&ukey=AAE42581AA0F57EC6B601F9DCECD1C9D&act=del&ip=all'

        # 发送HTTP GET请求
        response = requests.get(url)

        # 检查响应是否成功
        if response.status_code == 200:
            return "所有规则已成功删除"
        else:
            return f"HTTP请求失败，状态码: {response.status_code}"
    except Exception as e:
        return f"发生错误: {str(e)}"

def add_to_ip_whitelist(ip):
    try:
        # 构建请求URL来添加新规则
	#在{ip}前面写上你的添加白名单接口
	#示例 http://op.xiequ.cn/IpWhiteList.aspx?uid=XXXXX&ukey=XXXXX&act=add&ip={ip}
        url = 'http://op.xiequ.cn/IpWhiteList.aspx?uid=105964&ukey=AAE42581AA0F57EC6B601F9DCECD1C9D&act=add&ip={ip}'

        # 发送HTTP GET请求
        response = requests.get(url)

        # 检查响应是否成功
        if response.status_code == 200:
            return "IP地址已成功添加到白名单"
        else:
            return f"HTTP请求失败，状态码: {response.status_code}"
    except Exception as e:
        return f"发生错误: {str(e)}"

if __name__ == "__main__":
    public_ip = get_public_ip()

    if public_ip:
        # 先删除所有规则
        delete_result = delete_all_from_ip_whitelist()
        print(delete_result)

        # 添加新规则
        add_result = add_to_ip_whitelist(public_ip)
        print(add_result)
    else:
        print("无法获取外网IP地址")
