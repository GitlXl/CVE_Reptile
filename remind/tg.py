import requests
import time
from sql.cve_sql import *


def tg(cve_url,tg_xx,cveid,chat_id,bot_id,bot_ses,proxy):
    try:
        tg_url = "https://api.telegram.org:443/%s:%s/sendMessage"%(bot_id,bot_ses)
        tg_headers = {"POST /botxxxxxxxxxx": "xxxxxxxxxx/sendMessage HTTP/1.1", "User-Agent": "curl/7.68.0", "Accept": "*/*", "Content-Type": "application/x-www-form-urlencoded", "Connection": "close"}
        tg_xx = tg_xx.format("".encode("utf-8"))
        # test群
        proxies = {
                "http":"http://"+proxy,
                "https":"https://"+proxy,
                "https":"socks5h://"+proxy,
        }
        tg_data = "chat_id={3}&text={0}\n{1}\n{2}".format(cve_url,tg_xx,"%s"%cveid,chat_id).encode("utf-8")
        #requests.post(tg_url, headers=tg_headers, data=tg_data, proxies={"https":"socks5h://127.0.0.1:7891"}, verify=False,timeout=5)
        requests.post(tg_url, headers=tg_headers, data=tg_data, proxies=proxies, timeout=5)

    except Exception as e:
        print("访问TG代理地址有问题!!!")
        time.sleep(10)
        tg(cve_url,tg_xx,cveid,chat_id,bot_id,bot_ses,proxy)
