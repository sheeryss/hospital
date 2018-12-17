#coding=utf-8

import random
import urllib.request
import time
import re
#正则分析代理ip网页
def get_ip_list(html):
    listip = []
    ip = re.findall('<td data-title="IP">(.*?)</td>',html,re.S)
    port = re.findall('<td data-title="PORT">(.*?)</td>',html,re.S)
    for i in range(0,len(ip)):
        full_ip = ip[i] + ":" + port[i]
        listip.append(full_ip)
    return listip
#获取第cout页代理ip列表
def rep_list_ip(cout):
    try:
        ip_url = 'https://www.kuaidaili.com/free/inha/' + str(cout)+ '/'
        req = urllib.request.Request(ip_url)
        #print("request work")
        response = urllib.request.urlopen(req)
        #print("have response")
        req_html = response.read().decode('utf-8')
        time.sleep(2)
        list_ip = get_ip_list(req_html)
        return list_ip
    except:
        print ('rep_list_ip failed')
        return 0
    
    

      