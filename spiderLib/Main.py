#爬取主程序Main
from spiderLib import ParseOnePage
class Main(ParseOnePage.ParseOnePage):
    #爬取的main方法，用到了递归，目的为爬取无限层级的页面，不过前提是配置好ParamConf的参数
    #return：list
    def main(self, conf_param_len):
        #判断conf_param_len是否大于0
        if conf_param_len > 0:
            conf_param_len = conf_param_len - 1
            if len(self.get_list) > 0:
                #声明一个临时liat，用于存放新爬下来的数据
                get_list_temp = []
                for item in self.get_list:
                    item = item.strip()
                    if item[0:1] == "/":
                        item = self.domain_name+item
                    html = self.get_one_page(item)
                    get_list_temp += list(self.parse_one_page(html, len(self.conf_param)-conf_param_len-1, 1))
                #将临时list的数据赋给get_list
                self.get_list = get_list_temp
            else:
                #第一次进入，没有get_list值时走这里，然后就第一次爬取下来的数据存放到get_list中，一般在最后一层之前存放的都是url
                html = self.get_one_page()
                self.get_list = self.parse_one_page(html)
            #如果conf_param_len大于0，则递归
            self.main(conf_param_len)
        #递归出口
        return self.get_list
       
    
