#!/usr/bin/env python

'''
To read the .txt files inside the hotel folders and then append all those files into a single file 
in accordance to the name of the file
'''

import os 

def main() : 
	## reading the first file named "dark_ocr_menu_output"

	dark = '/home/tasdik/Dropbox/projects/big_data_project/test/dark_ocr_menu_output'
	light = '/home/tasdik/Dropbox/projects/big_data_project/test/light_ocr_menu_output'

	dest_file = '/home/tasdik/Dropbox/projects/big_data_project/test/first_600_restaurants_menus'

	### reading the dark first file 

	dark_hotels_list = os.listdir('/home/tasdik/Dropbox/projects/big_data_project/test/dark_ocr_menu_output')
	


if __name__ == '__main__' : 
	main()