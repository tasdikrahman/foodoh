#!/usr/bin/python

'''

crawl the menu's images of all the restaurants 

and, stores them in dictionary data structure where key will be the name of restaurant and value 
will be the list of menu's images. 

'''

import urllib2 
import threading
from bs4 import BeautifulSoup as bs

url = open("burrp_bangalore.txt","r").readlines()
img_links = open("image_links.txt","a")
for i in url:
	link_list=[]
	url=urllib2.urlopen(i).read()
	soup=bs(url,'lxml')
	div=soup.find("div",{"class":"MT15 menuList clearfix"})
	img=div.findAll("img",{"class":"menu-thumbnail"})

	for src in img:
		link_list.append(src.get("src"))

	dic={i.split("/")[-2]:link_list}
	print dic
	img_links.write(dic+"\n")
