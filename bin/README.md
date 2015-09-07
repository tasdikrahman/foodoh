## Big Data Project

## Restaurent Recommender

We are trying to build a restaurent recommender which will suggest you places according to the food you enter and the place you are currently in(the one you choose to)

Status : 
  * Date : 24-8-15
  	* got the list of restaurents near the bangalore area and stored the list in "burrp_bangalore.txt"
  	* using that list (burrp_bangalore.txt), made a scaper which would scrape the links of the menu's of those particular restaurents and store it in the form of a dictionary with the key as the name of the hotel and its value being a list containg the links to it's menu (.jpg files). Stored it in "image_links.txt"
  	* completed the menu scraper which is "all_images.py" which reads all the restaurent names from the file "image_links" and scrapes the menu images creating seperate folders for each of the restaurents.
