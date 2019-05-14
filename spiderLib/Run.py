#执行爬取动作类
from spiderLib import Main
class Run(Main.Main):
    def run(self):
        return self.main(len(self.conf_param))


