# 导入selenium模块中的web引擎
#coding=utf-8
#from selenium import webdriver
import urllib.request
import time
#import urllib
import re

#根据城市名称获取城市所有医院列表
def get_cityhtml(web_name, list_ip):
    i = 0
    print("开始获取城市医院列表.....")
    while(True):
        try:
            real_url = web_name
            proxy_support = urllib.request.ProxyHandler({'http': list_ip[i]}) #随机代理ip设置，避免单一ip过多访问服务器被拒绝

            opener = urllib.request.build_opener(proxy_support)
            opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36')]#给代理ip加上通行证

            urllib.request.install_opener(opener)
            req = urllib.request.Request(real_url)
            print("request work")
            response = urllib.request.urlopen(req, timeout=3)
            print("have response")
            req_html = response.read().decode('utf-8')
            print("return response")
            break
        except:
            time.sleep(2)
            i = i+1
            if(i>len(list_ip)):
                print ('no useful ip and change ip_list')
                req_html = 'not found'
                break
    return req_html
