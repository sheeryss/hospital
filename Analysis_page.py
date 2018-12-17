#可获得信息：医院名称、医院地址（省、市、县、街道）、联系电话、医院等级、重点科室、经营方式、医院网站

#coding=utf-8

import re

null = ['null']
def hop_name(hop_html):
    name = re.findall(r' href=".*?" title="(.*?)">', hop_html,re.S)
    if (name == []):
        return null
    return name

def second_name(hop_html):
    name2 = re.findall(r'</a>（(.*?)）</b>', hop_html,re.S)
    if (name2 == []):
        return null
    return name2

def hop_manage(hop_html):
    manage_way = re.findall(r'<li><b>经营方式</b>：(.*?)</li>', hop_html,re.S)
    if (manage_way == []):
        return null
    return manage_way

def hop_level(hop_html):
    level = re.findall(r'<li><b>医院等级</b>：(.*?)</li>', hop_html,re.S)
    if (level == []):
        return null
    return level
    
def hop_address(hop_html):
    address = re.findall(r'<li><b>医院地址</b>：(.*?)</li>', hop_html,re.S)
    if (address == []):
        return null
    return address

def hop_phone(hop_html):
    phone = re.findall(r'<li><b>联系电话</b>：(.*?)</li>', hop_html,re.S)
    if (phone == []):
        return null
    return phone

def hop_department(hop_html):
    department = re.findall(r'<li><b>重点科室</b>：(.*?)</li>', hop_html,re.S)
    if (department == []):
        return null
    return department

def hop_web(hop_html):
    web = re.findall(r'<li><b>医院网站</b>：<a href="(.*?)" ', hop_html,re.S)
    if (web == []):
        return null
    return web    