#coding = utf-8

#title：抓取某网页的所有链接并将链接编码后放入各个文件夹内

import re
import requests
import sys
import os
#定义页面链接，并抓取此页面的网页代码
r = requests.get('https://www.chinabidding.cn/search/searchzbw/search2?rp=22&categoryid=1&keywords=%E8%BD%A8%E9%81%93%E4%BA%A4%E9%80%9A&page=1&areaid=&table_type=0&b_date=year');
#把代码存入一个变量中
data = r.text
#print data;

#正则匹配需要抓取的链接
link_list =re.findall(r'target="_blank" href="(.+?\.html)' ,data)
#定义一个参数为0，方便循环编码
i=0
#开始循环
for url in link_list:
    #循环参数
    i=i+1
    #将参数变为字符串方便拼接
    ii = '%d'%i
    #在路径下创建编码的文件夹
    os.makedirs(r'd:/pythonWorkSpace/Python27PygamePy2exe-master/Python27PygamePy2exe-master/'+ii)
    #在目标文件夹下打开一个html页面并定于可以写入
    f = file('d:/pythonWorkSpace/Python27PygamePy2exe-master/Python27PygamePy2exe-master/'+ii+'/'+ii+".html", "w")
    #定义抓取的目标页面下的子链接的html代码
    url='https://www.chinabidding.cn'+url
    print url
    #抓取子链接代码
    r = requests.get(url)
    #编码转换，不转会报错，可以在此转，也可以用u'字符串'的形式转
    reload(sys)
    sys.setdefaultencoding('utf-8')
    #将html代码写入变量
    thisdata = r.text
    #将变量写入文件
    f.write(thisdata)
    #关闭文件
    f.close()
    #print thisdata
#执行时务必将中文去掉，否则会报字符编码的错
