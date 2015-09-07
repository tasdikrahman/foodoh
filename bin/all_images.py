#!/usr/bin/env python

'''
To scrape the links in all the menu images found from burpp

Note : Before running the script, change the value of the "img_dir_path" variable to 
	   the place where you need the image folders to be.
'''

import urllib
import os 

def main() : 
	with open('image_links_bangalore.txt', 'r') as f : 
		var = f.readlines()		
		lines = [x.strip('\n') for x in var]		
		### lines will be storing each individual lines as a list, with the newlines stripped from it.
		## now we have to iterate over it

		for line in lines : 
			## create the directory where the images would be stored 

			first_line_dict = eval(line)				## converted it to a dictionary

			image_links_key = first_line_dict.keys()
			var = image_links_key[0]
			image_links_key = var 							## stores the key

			#####    creating the required directory for the hotel  ######

			img_dir_path = '/home/tasdik/Dropbox/projects/big_data_project/test/images/' + str(image_links_key)

			''' 
			making the following if condition so that if the directory is already there, skip making that 
			particular directory.
			'''
			if os.path.exists(img_dir_path) : 
				continue
				
			if not os.path.exists(img_dir_path) : 
				os.makedirs(img_dir_path)

			## directory created , changing to that dir
			os.chdir(img_dir_path)
			print 'changed directory to : '+str(img_dir_path)

			#####		------------------------------------------- ######

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
