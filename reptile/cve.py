import re
from lxml import etree
from numpy import mat
from soupsieve import match
from sql.cve_sql import *


# 数据分析
def analysis(retext):
    retext = str(retext)
    re_xpath = etree.HTML(retext)
    en_text = re_xpath.xpath('/html/body//table[@cellpadding]/tr[4]/td[@colspan="2"]/text()')
    # print(en_text)
    regex = r"[a-zA-Z].*?\\n"
    matches = re.search(regex, str(en_text))
    matches_en = matches.group(0)
    print(matches_en)
    return matches_en