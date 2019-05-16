#爬取页面参数配置类
#param1:param_list(list)
from spiderLib import Base
class ParamConf(Base.Base):
    # 重写构造函数
    def __init__(self):
        self.get_list = []
        # #域名，用于和相对地址进行拼接
        # self.domain_name = "http://www.stdaily.com"
        # #conf_param参数为list其中第一项为爬取起始页，和爬取起始页的匹配规则
        # #中间项为爬取url的匹配规则
        # #最后一项是爬取最终页的匹配规则，这里写的匹配规则就是我们最后要得到的数据
        # #如果匹配的时候出错，请一定检查自己写的匹配规则！！！

        # #demo1
        # #下面的这个匹配是一个demo:http://www.stdaily.com/qykj/index.shtml
        # self.conf_param = [
        #     ['http://www.stdaily.com/qykj/index.shtml', '<div class="moretit"><h3>.*?<a href="(.*?)".*?</a>'],
        #     ['', '<div class="f_lieb_list">.*?<li>.*?<h3>.*?<a href="(.*?)".*?</a>'],
        #     ['', '<h1 class="ctitle">(.*?)</h1>.*?<div class="time">(.*?)<span']
        # ]

        #demo2
        #https://news.baidu.com/finance
        self.domain_name = "https://news.baidu.com"
        self.conf_param = [
            ['https://news.baidu.com/finance', '<li class="bold-item">.*?<a href="(.*?)".*?</li>'],
            ['', '<h3>.*?<a class="upgrade".*?href="(.*?)".*?</h3>'],
            ['', '<div class="article-title">.*?<h2>(.*?)</h2>']
        ]

