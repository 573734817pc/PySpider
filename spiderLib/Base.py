#基础类，定义了两个属性domain_name（域名，用于当爬下来的地址为相对地址时，拼接地址），conf_param（空list）
class Base(object):
    def __init__(self):
        self.domain_name = ""
        self.conf_param = []


