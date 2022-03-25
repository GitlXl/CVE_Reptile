import re
import time
from lxml import etree


# 包分析
def package_analysis(html_text,initial_cve):
    if "ERROR:" in html_text:
        print("CVE-2022-%s漏洞还没出生"%initial_cve)
        # initial_cve -= 1
        # time.sleep(520)
        return False
    else:
        print("新CVE-2022-%s漏洞诞生了"%initial_cve)
        return True

# 数据分析
def analysis(retext):
    retext = str(retext)
    re_xpath = etree.HTML(retext)
    # print(re_xpath)
    en_text = re_xpath.xpath('/html/body//table[@cellpadding]/tr[4]/td[@colspan="2"]/text()')
    regex = r"[a-zA-Z].*\."
    matches = re.search(regex, str(en_text))
    matches_en = matches.group(0)
    # print(matches_en)
    return matches_en