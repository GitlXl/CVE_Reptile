# /usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@File  :   CVE_Reptile.py
@Time  :   2022/03/08 22:28:25
@作者   :   Q狗
@优化   :   W狗
@GitHub:   https://github.com/GitlXl

不以物喜，不以己悲
'''

#自定义工具包
from mimetypes import init
import os
import datetime
import configparser

from zeroconf import InterfacesType
from reptile.send import send
from reptile.cve import analysis
from en_zh.en_zh_google import translate
from remind.tg import tg
from sql.cve_sql import *

# 获取配置文件内容
syspath = os.path.dirname(os.path.abspath(__file__))
conf = configparser.ConfigParser()
conf.read("./config.ini")

chat_id = conf.get("tgtest", "chat_id").strip()
bot_id = conf.get("tgtest", "bot_id").strip()
bot_ses = conf.get("tgtest", "bot_ses").strip()
proxy = conf.get("proxy", "socks5").strip()
# URL参数
cve_baseurl="https://cve.mitre.org:443/cgi-bin/cvename.cgi?name="
initial_cve = int(input("请输入目前开始的CVE编号:"))


# 爬取的三种情况
def find(html_text,cveid,initial_cve):
    if "ERROR:" in html_text:
        print("%s漏洞还没出生"%cveid)
        # 写入数据库
        time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data = (initial_cve,cveid, 0, 'null', time)
        insert_cve_2022_data(data)


    elif "This candidate has been reserved by an organization or individual that will use it when announcing a new security problem." in html_text:
        print("%s未公开"%cveid)
        # 写入数据库
        time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data = (initial_cve,cveid, 2, 'CVE编号未公开', time)
        insert_cve_2022_data(data)

    else:
        # 提权需要字段
        en_text = analysis(html_text)
        # 翻译为中文
        zh_text =  translate(en_text)
        # tg提醒，也可替换为其他提醒
        # if 数据库存在不发送提醒
        tg(cve_url,zh_text,cveid,chat_id,bot_id,bot_ses,proxy)
        # 写入数据库
        time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data = (initial_cve,cveid, 1, zh_text, time)
        insert_cve_2022_data(data)
        print("%s漏洞诞生了"%cveid)

if __name__ == "__main__":
    # 主要逻辑
    while initial_cve < 99999:
        if initial_cve < 10:
            initial_cve = "000"+str(initial_cve)
        elif initial_cve < 100:
            initial_cve = "00"+str(initial_cve)
        elif initial_cve < 1000:
            initial_cve = "0"+str(initial_cve)
        print(initial_cve)
        cveid = "CVE-2022-"+str(initial_cve)
        cve_url=cve_baseurl+cveid
        # 发送请求获得html源文件
        html_text = send(cve_url)
        # 转换类型
        initial_cve = int(initial_cve)
        # 判断三种情况
        find(html_text,cveid,initial_cve)
        # 循环加一
        initial_cve += 1