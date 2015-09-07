#!/usr/bin/env python

'''
To scrape the links in all the menu images found
'''

import urllib
import os 
from bs4 import BeautifulSoup as bs

def main() : 
	link_file_open = open('image_links_bangalore.txt', 'r')
	## create the directory where the images would be stored 

	img_dir_path = '/home/tasdik/Dropbox/projects/big_data_project/test/images'
	if not os.path.exists(img_dir_path) : 
		os.makedirs(img_dir_path)

	## directory created , changing to that dir
	os.chdir(img_dir_path)
	print 'changed directory'

	## read the links
	## testing for the first link 

	first_line = link_file_open.readline().strip()
	## divide the string into key and value and store it in two different variables
	## removing the {} character for easy easy division

	first_line_dict = eval(first_line)				## converted it to a dictionary

	image_links_key = first_line_dict.keys()
	var = image_links_key[0]
	image_links_key = var 							## stores the key

	image_links_values_list = first_line_dict[image_links_key]			##this is already a list 

	### replacing the height and width for the links 

	updated_links_values_list = [w.replace('?height=53&width=71', '') for w in image_links_values_list]
	i = 0 
	for link in updated_links_values_list : 				## iterate over the list 
		print link
		## downloading from the link 
		## image name 
		img_name = image_links_key + '_'+ str(i)+'.jpg'
		urllib.urlretrieve(link, img_name)
		i += 1

if __name__ == '__main__' : 
	main()
