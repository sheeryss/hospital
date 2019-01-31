#coding=utf-8

#输入：需要获得的代理IP页数（每页15个ip）
#输出：数组形式的代理IP值

import random
import urllib.request
import time
import re

class IpProxy(object):
    def __init__(self, cout):
        self.__web = 'https://www.kuaidaili.com/free/inha/'
        self.cout = cout

    def get_web(self):
        return self.__web

    #获取cout页代理ip列表
    def rep_ip(self):
        i = 1
        if(self.cout == 0):
            return 0
        for i in range(self.cout):
            ip_url = self.__web + str(i)+ '/'
            req = urllib.request.Request(ip_url)
            response = urllib.request.urlopen(req)
            try:
                req_html = response.read().decode('utf-8')
                print("response set")
                time.sleep(2)
                list_ip = self.get_ip_list(req_html)
                list_ip += list_ip
            except:
                print("failed")
        return list_ip
    #正则分析代理ip网页
    def get_ip_list(self, html):
        listip=[]
        ip = re.findall('<td data-title="IP">(.*?)</td>',html,re.S)
        port = re.findall('<td data-title="PORT">(.*?)</td>',html,re.S)
        for i in range(0,len(ip)):
            full_ip = ip[i] + ":" + port[i]
            listip.append(full_ip)
        return listip
    