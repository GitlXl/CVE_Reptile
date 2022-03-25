from traceback import print_tb
import requests
import time


def tg(cve_url,tg_xx,initial_cve,chat_id,bot_id,bot_ses,proxy):
    try:
        if tg_xx == "此候选人已被组织或个人保留，在宣布新的安全问题时将使用它。":
            print("进入存档")
            # file = open('002_未公布的CVE.txt', 'a')
            # str2 = 'CVE-2022-%s\n'%initial_cve
            # print(str2)
            # file.write(str2)
            # file.close()
        else:
            tg_url = "https://api.telegram.org:443/%s:%s/sendMessage"%(bot_id,bot_ses)
            tg_headers = {"POST /botxxxxxxxxxx": "xxxxxxxxxx/sendMessage HTTP/1.1", "User-Agent": "curl/7.68.0", "Accept": "*/*", "Content-Type": "application/x-www-form-urlencoded", "Connection": "close"}
            tg_xx = tg_xx.format("".encode("utf-8"))
            # test群
            proxies = {
                    "http":"http://"+proxy,
                    "https":"https://"+proxy,
                    "https":"socks5h://"+proxy,
            }
            tg_data = "chat_id={3}&text={0}\n{1}\n{2}".format(cve_url,tg_xx,"新的CVE-2022-%s"%initial_cve,chat_id).encode("utf-8")
            #requests.post(tg_url, headers=tg_headers, data=tg_data, proxies={"https":"socks5h://127.0.0.1:7891"}, verify=False,timeout=5)
            requests.post(tg_url, headers=tg_headers, data=tg_data, proxies=proxies, timeout=5)

    except Exception as e:
        print("访问TG代理地址有问题!!!")
        time.sleep(10)
        tg(cve_url,tg_xx,initial_cve,chat_id,bot_id,bot_ses,proxy)
