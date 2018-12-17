#coding=utf-8

import urllib.request
import time
import re

#获取城市列表
def get_ciity_list():
    try:
        key_word = {}
        url = 'http://www.a-hospital.com/w/%E5%85%A8%E5%9B%BD%E5%8C%BB%E9%99%A2%E5%88%97%E8%A1%A8'

        response = urllib.request.urlopen(url)
        #print("have response")
        req_html = response.read().decode('utf-8')
        print("have request")
        fulllist = re.findall(r'<p><b>(.*?)\n<h3><span', req_html,re.S)
        #print(fulllist)
        for i in range(0, len(fulllist)):
            city_list = re.findall(r'title="(.*?)">', fulllist[i], re.S)
            prin = city_list[0]
            del city_list[0]
            #print("have city_list")
            #print(prin)
            key_word[prin] = city_list
            #print(key_word)

            city_list = []
            prin = ''
            print("have key_word")
        print(len(key_word))
        return(key_word)
    except:
        time.sleep(3)
        get_ciity_list()
