#coding=utf-8

import re
import xlrd
import xlwt
import xlutils
from xlutils.copy import copy
from Analysis_page import *

#解析获取到的城市网页并获取保存每个医院的对应信息
def input_excel(city_html, city_name, city_number, book_name):

    #分解网页成一个个的医院列表
    hospital_list = re.findall(r'li><b><a(.*?)\n</ul>\n</li>', city_html, re.S)
    #print('hospital_list is : ')
    #print(hospital_list)
    list_num = 1
    message = []
    #分解医院成一个个信息
    for each_hospital in hospital_list:
        message = hop_name(each_hospital) + second_name(each_hospital) + hop_manage(each_hospital) + hop_level(each_hospital) + hop_address(each_hospital) + hop_phone(each_hospital) + hop_department(each_hospital) + hop_web(each_hospital)
        #print('message is')
        #print('保存中。。。。')
        row = list_num
        hop_book1 = xlrd.open_workbook(book_name)
        hop_book = copy(hop_book1)
        sheet = hop_book.get_sheet(city_number)
        for col in range(0,len(message)):
            sheet.write(row, col, message[col])
        hop_book.save(book_name)
        list_num += 1