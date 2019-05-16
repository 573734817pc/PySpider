#正则匹配页面元素类
from spiderLib import GetOnePage
import re
class ParseOnePage(GetOnePage.GetOnePage):
    #爬取页面元素方法：parse_one_page
    # param1:html(string)
    # param1:key1(int)
    # param1:key2(int)
    # return:items(tuple)
    def parse_one_page(self, html, key1=0, key2=1):
        pattern = re.compile(self.conf_param[key1][key2], re.S)
        if html == "":
            items = []
        else:
            items = re.findall(pattern, html)
        return items

