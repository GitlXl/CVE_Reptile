import requests
import jsonpath

def translate(matches_en):
    count = 5
    try:
        # 请求翻译接口
        translate_url = "https://translate.googleapis.com:443/translate_a/single?client=gtx&sl=auto&tl=zh-cn&hl=en-US&dt=t&dt=bd&dj=1&source=input&q=%s moring&tk=281129.281129"%matches_en
        translate_headers = {"Sec-Ch-Ua": "\"(Not(A:Brand\";v=\"8\", \"Chromium\";v=\"98\"", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36", "Sec-Ch-Ua-Platform": "\"Linux\"", "Accept": "*/*", "Sec-Fetch-Site": "none", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9"}
        while count > 0  :
            translate_re = requests.get(translate_url, headers=translate_headers)
            # , proxies={"https":"https://127.0.0.1:8080"}, verify=False
            if translate_re.status_code == 200:
                s = jsonpath.jsonpath(translate_re.json(),"$.sentences[0].trans")
                zh_text = "".join(s)
                print(zh_text)
                return zh_text
            count -= 1
        #翻译不成功
        return matches_en
    except Exception as e:
        print("翻译接口有问题!!!")
        #翻译不成功
        return matches_en