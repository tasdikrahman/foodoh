import urllib2
import re
from bs4 import BeautifulSoup as bs
# import pymongo
# client=pymongo.MongoClient()
# db=client['hotels']
i=1
dic={}

f  = open('ratings_out_of_five.txt', 'a')

while(i<=89):
	url=urllib2.urlopen("http://www.burrp.com/bangalore/restaurants/"+str(i)).read()
	soup=bs(url)
	div=soup.find("div",{"class":"colL"})
	ul=div.find("ul",{"class":"item_listing"})
	li=ul.findAll("li")
	for j in range(len(li)):
		try : 	
			y=li[j].find("a").get("title")
			x="hotelname"
			temp={filter(lambda t: ord(t)>31 and ord(t)<128, x):filter(lambda t: ord(t)>31 and ord(t)<128,y)}   

			dic.update(temp)

			href = li[j].find("a").get("href")
			ide = href.split("/")[-1]
			dic.update({"hotel_id" : str(ide)})

			div2=li[j].find("div",{"class":"lg_col MT5"})
			p=div2.findAll("p")
			

			if(p[0].getText()):
				x="rating"
				y=p[0].getText()
				temp={filter(lambda t: ord(t)>31 and ord(t)<128, x):filter(lambda t: ord(t)>31 and ord(t)<128,y)}   
			 	dic.update(temp)
			if(p[1].getText()):
				x="totalvotes"
				y=p[1].getText()
				temp={filter(lambda t: ord(t)>31 and ord(t)<128, x):filter(lambda t: ord(t)>31 and ord(t)<128,y)}   
			 	dic.update(temp)
			print dic
			f.write(str(dic) + '\n')
		# try:
  #       		dic.pop("_id")
  #   		except:
  #       		pass
		# db.cd.insert(dic)
		except Exception as e: 
			print 'NA rating'
	
	print "****************************************************************88"
	print i 
	print "******************************************************************"
	i=i+1
	
