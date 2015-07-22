# -*- coding: utf-8 -*-
import os
import os.path
import sys
reload(sys)
sys.setdefaultencoding("utf-8")  #开奖日期中的字符需要引入
import urllib2
from bs4 import BeautifulSoup

# 创建/打开一个文件放数据
def  fetchLottery():
 if os.path.exists("lottery.txt"):
	os.remove("lottery.txt")
 f = open("lottery.txt", "a")
 for i in range(3,16):
  print("正在获取"+"{:0>2d}".format(i)+"年数据")
  url = "http://www.lecai.com/lottery/draw/list/50?type=range_date&start=20"+"{:0>2d}".format(i)+"-01-01&end=20"+"{:0>2d}".format(i)+"-12-31"
  page = urllib2.urlopen(url)                                 # 打开目标url
  soup = BeautifulSoup(page,"html.parser")# 格式化标签
        #print(soup.find_all(attrs={"class":"historylist"}))
  foundAllTbody = soup.findAll(attrs={"class":"balls"})
  foundDate = soup.findAll("tbody")[0]
  num = 1
  if(foundAllTbody):
    for foundBalls in foundAllTbody[0:]:	
     foundAllTr = foundBalls.findAll("em")
     if(foundAllTr):
       ballStr = ""
       for foundTd in foundAllTr[0:]:
        if(foundTd):
         	ballStr += ","
         	ballStr += foundTd.string
         	  #print(foundTd.string)  
     date = foundDate.findAll("td")[(num-1)*10+num].string   #开奖日期
     f.write(date + "\t"+ ballStr+"\n")
     #print(foundDate.findAll("td")[(num-1)*10+num].string)
     num = num + 1    
 print "数据抓取完成"
 f.close()

fetchLottery()
