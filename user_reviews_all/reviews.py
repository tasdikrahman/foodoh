#!/usr/bin/python
from simplejson import loads 
from bs4 import BeautifulSoup
import requests
import threading 
import MySQLdb

# db = MySQLdb.connect("localhost","root","root","burrp")
# cursor = db.cursor()

rvwfileobj=open("reviews2.txt","a")
name_file_obj=open("burrp_bangalore.txt","r").readlines()

for url in range(12,len(name_file_obj)):
	post_id=name_file_obj[url].split('/')[-1].strip()
	print post_id
	urlmain=""
	
	for i in range(0,382):
		try :
		#global urlmain
			
			urlmain="http://www.burrp.com/bangalore/listings/getmorereviews?start="+str(i)+"&post_id="+str(post_id)+"&post_type=ESTABLISHMENT&shareUrl="+str(name_file_obj[url])+"&sort=latest"
			html = requests.get(urlmain)
				

			json = loads(html.content)
			if json.get('status'):
				try:
					dic={}
					soup =  BeautifulSoup(json.get('result'),'lxml')
					
					t = soup.find('p',{'id':'title'})
					ttl = t.text.lower()
					ttl=str(filter(lambda x:ord(x)>31 and ord(x)<128,ttl))

					
					
					dic.update({"title":ttl.strip()})
					
					rw = soup.find('p',{'id':'body'})
					rvw = rw.text.strip().lower()
					rvw=str(filter(lambda x:ord(x)>31 and ord(x)<128,rvw))
					
					#print rvw
					

					dic.update({"review":rvw})

					rt = soup.find('span',{'class':'star59x55 FR'})
					j = rt.text.strip()
					
					k = float(j)
					
					
					dic.update({"score":k})
					dic.update({"hotel":post_id})

					rvwfileobj.write(str(dic)+"\n")
			

				except Exception as e:
					print "INSIDE "
					print e
			else:
				break

			
		except Exception as e:
	
			print e
'''
	i=0
	while True:
		print i
		if threading.activeCount()<25:
			print "inside threading"
			t = threading.Thread(target= main, args=(i,))
			t.start()
			i+=1
'''

	#sql = "INSERT INTO hotel (`tittle`,`review`,`rating`) VALUES ('%s','%s','%f') ;" %(MySQLdb.escape_string(ttl),MySQLdb.escape_string(rvw),(k))
	#cursor.execute(sql)
	#db.commit()

