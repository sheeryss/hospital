#coding=utf-8

import urllib
import string
import xlrd
import xlutils
import openpyxl
import xlwt 

from urllib.parse import quote
from xlutils.copy import copy
import get_hop_html
from get_ip import *
from Analysis_page import *
from Getcitylist import get_ciity_list
import Gehopmessage
if __name__ == "__main__":
    A_hospital = "http://www.a-hospital.com/w/" 
    city_number = 0

    #爬取省市字典（省：多个城市）
    province_list = get_ciity_list()
    print(".................................................................")
    print(province_list)
    for prov in province_list.keys():
        city_number = 0
        print('in for')
        prin = prov + '.xls'
        city_list = province_list[prov]
        #创建信息表（xls）
        hop_book = xlwt.Workbook()
        i = 0
        for city in city_list:
            sheet = hop_book.add_sheet(city)
            i += 1
        hop_book.save(prin)
        city_name = city_list[0]
        print('set cityname success')
        #制作信息表模板
        for i in range(0,len(city_list)):
            add_first = xlrd.open_workbook(prin)
            add_name = copy(add_first)
            sheet = add_name.get_sheet(i)
            sheet.write(0, 0, '医院注册名称')
            sheet.write(0, 1, '医院别名')
            sheet.write(0, 2, '经营方式')
            sheet.write(0, 3, '医院等级')
            sheet.write(0, 4, '医院地址')
            sheet.write(0, 5, '联系方式')
            sheet.write(0, 6, '重点科室')
            sheet.write(0, 7, '官方网站')
            add_name.save(prin)
        #分析、加工、保存
        for city_name in city_list:
            #制作城市列表URL
            c_url = A_hospital + city_name
            URL = quote(c_url, safe =string.printable)
            cout = 1
            while(True):
                #获取代理ip
                proxy_ip = rep_list_ip(cout)
                print("代理ip获取成功........")

                #获取网页
                city_html = get_hop_html.get_cityhtml(URL, proxy_ip)
                print("compare response")
                if(city_html != 'not found'):
                    #time.sleep(2)
                    print('网页获取成功' + city_name)
                    break
                cout += 1
            print('保存中。。。。')
            Gehopmessage.input_excel(city_html, city_name, city_number, prin)
            city_number += 1
    print('work done..........')
