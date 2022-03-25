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
import os
import configparser
from reptile.send import *
from reptile.cve import *
from en_zh.en_zh_google import translate
from remind.tg import *


if __name__ == "__main__":
    # 获取配置文件内容
    syspath = os.path.dirname(os.path.abspath(__file__))
    conf = configparser.ConfigParser()
    conf.read("./config.ini")

    chat_id = conf.get("tgtest", "chat_id").strip()
    bot_id = conf.get("tgtest", "bot_id").strip()
    bot_ses = conf.get("tgtest", "bot_ses").strip()
    proxy = conf.get("proxy", "socks5").strip()

    # 主要逻辑
    cve_baseurl="https://cve.mitre.org:443/cgi-bin/cvename.cgi?name=CVE-2022-"
    initial_cve = int(input("请输入目前开始的CVE编号:"))
    while initial_cve < 99999:
        cve_url=cve_baseurl+str(initial_cve)
        # 发送请求获得html源文件
        html_text = send(cve_url)
        if package_analysis(html_text,initial_cve) == True:
            # 提取需要字段
            en_text = analysis(html_text)
            # 翻译为中文
            zh_text =  translate(en_text)
            # tg发送消息
            tg(cve_url,zh_text,initial_cve,chat_id,bot_id,bot_ses,proxy)
        initial_cve += 1