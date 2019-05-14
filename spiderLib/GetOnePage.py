#获取页面类
from spiderLib import ParamConf
import requests
from requests.exceptions import RequestException
class GetOnePage(ParamConf.ParamConf):
    # 爬取页面元素方法：parse_one_page
    # param1:url(string)
    # return:response.text(string)
    def get_one_page(self, url=""):
        try:
            if url != "":
                response = requests.get(url)
            else:
                response = requests.get(self.conf_param[0][0])
            response.encoding = response.apparent_encoding
            if response.status_code == 200:
                return response.text
            return None
        except RequestException:
            return None
